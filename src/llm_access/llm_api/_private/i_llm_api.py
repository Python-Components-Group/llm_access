from abc import ABC, abstractmethod



class ILlmApi(ABC):
	"""
		Represents an API, or inference platform, for LLMs.
        Each ILlmApi is immutable.
		
		Each ILlmApi is hashable (via `.__hash__(...)`) and comparable
        (via `.__eq__(...)`)
        
        The represented LLM API is specified by the descendants of this interface.
	"""
	
	
	@abstractmethod
	def api_name(self) -> str:
		"""
			Returns the name that identifies the represented API/platform
            
            Returns
            -------
                str
                    A lowercase string containing the name of the API/platform represented
                    by the descendants of this interface
		"""
		pass