from abc import ABC, abstractmethod
from .. import ILlmHyperParamId



class ILlmHyperParamIdFactory(ABC):
	"""
		Represents a factory for each `ILlmHyperParamId`.
        
        The models and/or specific APIs to which the instantiated hyperparameters
        belong are described by the descendants of this interface.
	"""
	
	
	@abstractmethod
	def create(
			self,
			param_id: str,
	) -> ILlmHyperParamId:
		"""
			Instantiates a new hyperparameter identifier, associated with the platform/models
            described by the descendants of this interface
            
            Parameters
            ----------
                param_id: str
                    A string containing the name of the hyperparameter to be requested
					
			Returns
            -------
                ILlmHyperParamId
                    An `ILlmHyperParamId` object, associated with the platform/LLMs specified by the descendants
                    of this interface, representing the requested hyperparameter
					
			Raises
            ------
                ValueError
                    Occurs if:
                    
                        - The provided `param_id` parameter has a value of `None`
                        - The provided `param_id` parameter is an empty string
						
				NotImplementedError
                    Occurs if the requested hyperparameter identifier is not implemented in GenTestsAI,
                    for the platform/models specified by the descendants of this interface
		"""
		pass
		
		
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================