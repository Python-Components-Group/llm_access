from .. import ILlmSpecImplFactory
from ...variability.combinatorial import EPlatformCombo

from .._factory.ollama_specimpl_f import OllamaSpecImplFactory



class LlmSpecImplFactoryResolver:
	"""
		Represents a factory of `ILlmSpecImplFactory`
	"""
	
	
	@classmethod
	def resolve(
			cls,
	        platforms: EPlatformCombo
	) -> ILlmSpecImplFactory:
		"""
			Instantiates a new `ILlmSpecImplFactory` for the requested platform combination
            
            Parameters
            ----------
                platforms: EPlatformCombo
                    An `EPlatformCombo` value representing the platforms for which to obtain the factory
					for specific LLM implementations.
            
            Returns
            -------
                ILlmSpecImplFactory
                    An `ILlmSpecImplFactory` object that allows instantiating specific implementations
                    of LLMs for the requested platform combination
					
			Raises
            ------
                NotImplementedError
                    Occurs if the factory for the requested platform combination is not
                    currently implemented, or does not exist, in the "llm_access" component
		"""
		obj_f: ILlmSpecImplFactory
		
		match platforms:
			case EPlatformCombo.OLLAMA:
				obj_f = OllamaSpecImplFactory()
			case _:
				raise NotImplementedError()
			
		return obj_f
		
		
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================