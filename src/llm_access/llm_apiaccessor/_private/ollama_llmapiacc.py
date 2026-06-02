from typing import List, Dict, Iterator, Any
from ._a_base_llmapiacc import _ABaseLlmApiAccessor

from base64 import b64encode as b64_encode
from ollama import (
	Client as OllamaClient,
	ChatResponse,
	ResponseError as OllamaApiResponseError
)
from time import monotonic as time_monotonic
from httpx import (
	Timeout as HttpxTimeout,
	TimeoutException as HttpxTimeoutError,
	ConnectTimeout as HttpxConnectTimeoutError
)

from ...llm_api import (
	ILlmApi,
	OllamaApi
)
from ...llm_chat import ILlmChat
from ...llm_hyperparam.id import (
	ILlmHyperParamId,
	LlmHyperParamIdFactoryResolver,
)
from ...llm_hyperparam import ILlmHyperParam
from ...llm_specimpl import ILlmSpecImpl


from c23_logger import ATemporalFormattLogger
from c23_logger.exceptions import FormatNotSetError

from ..exceptions import (
	ApiConnectionError,
	ApiResponseError,
	ResponseTimedOutError,
	SaturatedContextWindowError
)



class OllamaLlmApiAccessor(_ABaseLlmApiAccessor):
	"""
		Represents an `ILlmApiAccessor` for the "Ollama" inference platform.
        
        The following steps of the entire LLM request phase are logged:
			- Start of connection attempt
            - Connection attempt successfullness
            - Start of the response reception sub-phase
            - Each "chunk" of the received response (only if requested)
            - End of the response reception sub-phase
	"""
	
	def __init__(
			self,
			address: str,
			auth: str,
			conn_timeout: int,
			logger: ATemporalFormattLogger = None,
			log_resp: bool = False,
			logger_sep: str="\n",
	):
		"""
			Creates a new OllamaLlmApiAccessor and associates it with the first chat to be used
            to make requests
            
            Parameters
            ----------
				address: str
                    A string containing the address (absolute URL, IPv4, or IPv6) that identifies
                    the Ollama server hosting the inference platform
                    
                auth: str
                    A string containing the login credentials, such as a `user:token` pair,
					to be used for interactions
                
                conn_timeout: int
                    An integer representing the timeout in milliseconds after which to declare a connection attempt as failed
                    
                logger: ATemporalFormattLogger
					Optional. Default = `None`. An `ATemporalFormattableLogger` object representing the logger to be used to log the steps performed by this OllamaLlmApiAccessor during each request made.
                
                logger_sep: str
                    Optional. Default = `\\n`. A string containing the separator to use for the
                    logging messages that will be recorded.
                    
                log_resp: bool
                    Optional. Default = `False`. A boolean indicating whether to also log
                    the response "chunks" that are received
		
			Raises:
            ------
                ValueError
                    Occurs if:
                        
                        - At least one of `address` or `auth` is `None`
                        - The `log_resp` parameter is `True` but no logger has been provided
		"""
		super().__init__()
		
		self._logger: ATemporalFormattLogger = logger
		if logger is not None:
			self._logger_sep = logger_sep if logger_sep is not None else "\n"
		
		if log_resp and (logger is None):
			raise ValueError()
		if (address is None) or (auth is None):
			raise ValueError()
		
		self._log_resp: bool = log_resp
		self._o_addr: str = address
		self._o_auth: str = b64_encode(auth.encode()).decode()
		self._conn_tout: int = conn_timeout
		
		self._think_param: ILlmHyperParamId = LlmHyperParamIdFactoryResolver.resolve("ollama").create("think")
		self._numctx_param: ILlmHyperParamId = LlmHyperParamIdFactoryResolver.resolve("ollama").create("context_window")
	
	
	def _ap__prompt_spec(
			self,
			chat: ILlmChat,
			model: ILlmSpecImpl,
			hparams: List[ILlmHyperParam],
			timeout: int,
	) -> str:
		options_param: Dict[str, Any] = {
			hparam.param_id().id(): hparam.to_effvalue()
			for hparam in hparams
		}
		think_param: bool = options_param.pop(self._think_param.id())
		num_ctx_param: int = options_param[self._numctx_param.id()]
		
		conn_timeout: HttpxTimeout = HttpxTimeout(
			None, connect=int(self._conn_tout) / 1000.0
		)
		resp_timeout: float = timeout / 1000.0

		def_time_format: str = "( {day}-{month}-{year} | {hour}:{min}:{second} )"
		log_format: str = None
		if self._logger is not None:
			try:
				log_format = self._logger.unset_format()
				self._logger.set_format(log_format)
			except FormatNotSetError:
				self._logger.set_format("[LLM REQUEST (Ollama)] {message} " + def_time_format)
				
			self._logger.set_messages_sep(self._logger_sep)
			self._logger.log("Attempting to connect to Ollama ...")
			
		oll_client: OllamaClient
		try:
			oll_client = OllamaClient(
				host=self._o_addr,
				headers={ 'Authorization': f'Basic {self._o_auth}' },
				timeout=conn_timeout
			)
			if self._logger is not None:
				self._logger.log("Connection to Ollama established.")
		except HttpxConnectTimeoutError as httpx_tout_error:
			gensai_exc: ApiConnectionError = ApiConnectionError()
			gensai_exc.args = ("timeout",) + httpx_tout_error.args
			raise gensai_exc from httpx_tout_error
		except ConnectionError as ollama_err:
			gensai_exc: ApiConnectionError = ApiConnectionError()
			gensai_exc.args = ("other",) + ollama_err.args
			gensai_exc.errno = ollama_err.errno
			raise gensai_exc from ollama_err
		
		response_iter: Iterator[ChatResponse]
		try:
			response_iter = oll_client.chat(
				model.model_name(),
				chat.chat_messages(),
				options=options_param,
				stream=True,
				think=think_param,
			)
		except OllamaApiResponseError as ollama_err:
			gensai_exc: ApiResponseError = ApiResponseError()
			gensai_exc.args = ("known",) + ollama_err.args
			raise gensai_exc from ollama_err
		
		start_time: float
		timed_out: bool = False
		drifted: bool = False
		prompt_tokens: int = -1
		resp_tokens: int = -1
		full_response: str = ""
		try:
			self._logger.log("Start of response ...") if self._logger is not None else None
			if self._log_resp:
				log_format = self._logger.unset_format()
				self._logger.set_messages_sep("")
				
			start_time = time_monotonic()
			for chunk in response_iter:
				full_response += chunk['message']['content']
				if self._log_resp:
					self._logger.log(chunk['message']['content'])
				
				# Check del tempo complessivo occupato dalla risposta fino ad ora
				if ((time_monotonic() - start_time) > resp_timeout):
					timed_out = True
					break
				
				# Se è arrivato alla fine
				if "eval_count" in chunk:
					resp_tokens = chunk["eval_count"]
					prompt_tokens = chunk["prompt_eval_count"]
					if self._log_resp:
						self._logger.log(f'{self._logger_sep}')
							
			if timed_out or drifted:
				if self._log_resp:
					self._logger.set_format(log_format)
					self._logger.set_messages_sep(self._logger_sep)
				if timed_out:
					raise ResponseTimedOutError()
		except HttpxTimeoutError as httpx_tout_err:
			gensai_exc: ResponseTimedOutError = ResponseTimedOutError()
			gensai_exc.args = httpx_tout_err.args
			raise gensai_exc from httpx_tout_err
		except OllamaApiResponseError as ollama_err:
			gensai_exc: ApiResponseError = ApiResponseError()
			gensai_exc.args = ("known",) + ollama_err.args
			raise gensai_exc from ollama_err
		
		if self._log_resp:
			self._logger.set_format(log_format)
			self._logger.set_messages_sep(self._logger_sep)
		self._logger.log(f'End of response.') if self._logger is not None else None

		if ((prompt_tokens == -1) or (resp_tokens == -1) or
			(full_response == "")):
			gensai_exc: ApiResponseError = ApiResponseError()
			gensai_exc.args = ("unknown",) + (str(prompt_tokens), str(resp_tokens), full_response)
			raise gensai_exc

		if (prompt_tokens + resp_tokens) >= num_ctx_param:
			raise SaturatedContextWindowError()
		
		return full_response
	
	
	def _ap__accepted_api(self) -> ILlmApi:
		return OllamaApi()


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================