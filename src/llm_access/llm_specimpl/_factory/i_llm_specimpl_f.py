from abc import ABC, abstractmethod
from .. import ILlmSpecImpl

from ...variability import ESpecLlmImpl



class ILlmSpecImplFactory(ABC):
	"""
		Represents a factory for each `ILlmSpecImpl`.
        
        The API specifications associated with the instantiated specific implementations
        are described by the subclasses of this interface
	"""
	
	
	@abstractmethod
	def create(
			self,
			model: ESpecLlmImpl,
	) -> ILlmSpecImpl:
		"""
			Instantiates a new platform-specific implementation associated with the platforms described by the descendants of this interface

			Parameters
			----------
                model: ESpecLlmImpl
                    A `ESpecLlmImpl` value representing the specific implementation of the
					Large Language Model from which to obtain the `ILlmSpecImpl` object;
            
            Returns
            -------
                ILlmSpecImpl
                    A `ILlmSpecImpl` object, bound to the platforms specified by the descendants
					of this interface, representing the specific LLM implementation requested
            
            Raises
            ------
                ValueError
                    Occurs if:
                    
                        - The provided `model` parameter is `None`
						- The provided `model` parameter is an empty string
                
                NotImplementedError
                    Occurs if the requested LLM implementation is not implemented in the component
                    for the combination of platforms specified by the descendants of this interface
		"""
		pass
		
		
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================