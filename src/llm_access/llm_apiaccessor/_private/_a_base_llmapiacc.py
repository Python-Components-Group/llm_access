from typing import List, Set
from abc import abstractmethod
from .. import ILlmApiAccessor

from ...llm_api import ILlmApi
from ...llm_chat import ILlmChat
from ...llm_hyperparam import ILlmHyperParam
from ...llm_hyperparam.id import ILlmHyperParamId
from ...llm_specimpl import ILlmSpecImpl

from ..exceptions import (
	ChatNeverSelectedError,
	ModelNotSelectedError,
	IncompatibleApiError,
	IncompatibleHyperparamError,
	HyperparamNotExistsError,
	HyperparamAlreadyExistsError
)



class _ABaseLlmApiAccessor(ILlmApiAccessor):
	"""
		Represents a base `ILlmApiAccessor`, containing the control logic common to every `ILlmApiAccessor`.
        
        The specific API associated is described by the descendants of this abstract class.
	"""
	
	def __init__(self):
		"""
			Creates a new _ABaseLlmApiAccessor
		"""
		self._erase_chat: bool = False
		self._model: ILlmSpecImpl = None
		self._hparams: List[ILlmHyperParam] = list()
		self._repr_api: ILlmApi = None
		self._chat: ILlmChat = None
	
	
	def set_chat(
			self,
			chat: ILlmChat,
			erase_now: bool = True,
			erase_model: bool = True
	):
		if chat is None:
			raise ValueError()
		
		if self._repr_api is None:
			self._repr_api = self._ap__accepted_api()
		if self._repr_api not in chat.compat_apis():
			raise IncompatibleApiError()
		
		self._chat = chat
		if erase_now:
			self._chat.clear()
		self._erase_chat = erase_model
	
	
	def select_model(
			self,
			model: ILlmSpecImpl
	):
		if model is None:
			raise ValueError()
		if self._chat is None:
			raise ChatNeverSelectedError()
		if self._repr_api not in model.compat_apis():
			raise IncompatibleApiError()
		
		self._model = model
		self._hparams.clear()
		if self._erase_chat:
			self._chat.clear()
	
	
	def add_hyperparam(self, hparam: ILlmHyperParam):
		if hparam is None:
			raise ValueError()
		if self._chat is None:
			raise ChatNeverSelectedError()
		if self._model is None:
			raise ModelNotSelectedError()
		if self._model.model_hyperparams().intersection({hparam.param_id()}) == {}:
			raise IncompatibleHyperparamError()
		
		set_ids: Set[ILlmHyperParamId] = {hparam_c.param_id() for hparam_c in self._hparams}
		if hparam.param_id() in set_ids:
			raise HyperparamAlreadyExistsError()
		
		self._hparams.append(hparam)
	
	
	def remove_hyperparam(self, hparam: ILlmHyperParam):
		if hparam is None:
			raise ValueError()
		if self._chat is None:
			raise ChatNeverSelectedError()
		if self._model is None:
			raise ModelNotSelectedError()
		
		list_ids: List[ILlmHyperParamId] = [hparam_c.param_id() for hparam_c in self._hparams]
		if hparam.param_id() not in list_ids:
			raise HyperparamNotExistsError()
		
		to_remove: int = list_ids.index(hparam.param_id())
		self._hparams.pop(to_remove)
	
	
	def prompt(
			self,
			timeout: int
	) -> str:
		if self._chat is None:
			raise ChatNeverSelectedError()
		if self._model is None:
			raise ModelNotSelectedError()
		if timeout < 1:
			raise ValueError()
		
		response: str = self._ap__prompt_spec(
			self._chat,
			self._model,
			self._hparams,
			timeout
		)
		self._chat.add_response(response)
		
		return response
	
	
	#	============================================================
	#						ABSTRACT METHODS
	#	============================================================


	@abstractmethod
	def _ap__prompt_spec(
			self,
			chat: ILlmChat,
			model: ILlmSpecImpl,
			hparams: List[ILlmHyperParam],
			timeout: int
	) -> str:
		"""
			Performs a single interaction with the selected model via the associated API/platform,
			passing the last prompt set in the `ILlmChat` object provided.
            
            The following conditions are guaranteed within this method:
				- That `timeout >= 1`
                - That the `user_prompt` parameter is neither `None` nor an empty string
                - That the `model` is accepted by the API
                - That every hyperparameter in `hparams` is valid for the `model`
			
			Parameters
            ----------
                chat: ILlmChat
                    An `ILlmChat` object representing the chat to be used for
                    interacting with the model
					
				model: ILlmSpecImpl
                    An `ILlmSpecImpl` object representing the LLM with which to interact
                    
                hparams: List[ILlmHyperParam]
					An `ILlmHyperParam` object representing the list of hyperparameters to be used
                    in this interaction
                    
                timeout: int
                    An integer representing the timeout in milliseconds after which
                    the response is declared failed
				
			Returns
            -------
                str
                    A string containing the model's response to the interaction

            Raises
            ------
				InvalidPromptError
                    Occurs if `user_prompt` is invalid for the represented API
                    
                ApiConnectionError
                    Occurs if a connection error occurs with the inference platform.
                    The error belongs to its domain.
					The `args[0]` attribute, of type string, is used to distinguish the nature of the error:
                    
                        - "timeout": The nature of the error relates to a connection timeout
                        - "other": The nature of the error is of another type (as indicated by the other components of the `args` attribute)
				
				ResponseTimedOutError
                    Occurs if the specified `timeout` expires and no part of the response has been received
					
				ApiResponseError
                    Occurs if the request sent to the API produces a response error
                    belonging to its domain.
                    The `args[0]` attribute, of type string, is used to distinguish the nature of the error:
					
						- "known": The nature of the error is described by the inference platform
                        - "unknown": The nature of the error is not described by the inference platform and is unknown
                    
                SaturatedContextWindowError
                    Occurs if the context window becomes saturated during the interaction
		"""
		
		
	@abstractmethod
	def _ap__accepted_api(self) -> ILlmApi:
		"""
			Returns the object that identifies the API associated with this ILlmApiAccessor.
            
            Returns
            -------
                ILlmApi
                    An `ILlmApi` object representing the identifier of the API
                    associated with this ILlmApiAccessor
		"""
		pass
		
		
	#	============================================================
	#						PRIVATE METHODS
	#	============================================================