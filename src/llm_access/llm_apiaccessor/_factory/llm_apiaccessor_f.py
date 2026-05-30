from .. import ILlmApiAccessor

from c23_logger import ATemporalFormattLogger

from .._private.ollama_llmapiacc import OllamaLlmApiAccessor



class LlmApiAccessorFactory:
	"""
		Represents a factory for each `ILlmApiAccessor`
	"""


	@classmethod
	def for_ollama(
			cls,
			address: str,
	        auth: str,
	        conn_timeout: int,
	        logger: ATemporalFormattLogger = None,
	        log_resp: bool = False,
	        logger_sep: str = "\n"
	) -> ILlmApiAccessor:
		"""
			Instantiates a new accessor for the "Ollama" inference platform
            
            Parameters
            ----------
				address: str
                    A string containing the address (absolute URL, IPv4, or IPv6) that identifies
                    the server hosting the inference platform
                    
                auth: str
                    A string containing login credentials, such as a `user:token` pair,
					to be used for interactions
                
                conn_timeout: int
                    An integer representing the timeout in milliseconds after which to declare
                    a connection attempt as failed
                    
                logger: ATemporalFormattLogger
					Optional. Default = `None`. An `ATemporalFormattableLogger` object representing
					the logger to be used to log the steps performed by the instantiated
					`ILlmApiAccessor` during each request made.
                
                logger_sep: str
                    Optional. Default = `\\n`. A string containing the separator to use for the
                    logging messages that will be recorded.
                    
                log_resp: bool
                    Optional. Default = `False`. A boolean indicating whether to also log
                    the response "chunks" that are received
					
			Returns:
            -------
                ILlmApiAccessor
                    An `ILlmApiAccessor` object that provides access to the "Ollama" inference platform
					
			Raises
            ------
                ValueError
                    Occurs if:
                        
                        - At least one of `address` or `auth` is `None`
                        - The `log_resp` parameter is `True` but no logger has been provided
		"""
		return OllamaLlmApiAccessor(
			address, auth,
			conn_timeout,
			logger, log_resp, logger_sep
		)
		
		
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================