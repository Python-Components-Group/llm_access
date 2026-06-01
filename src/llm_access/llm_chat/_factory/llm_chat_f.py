from .. import ILlmChat
from .e_llmchatapis import ELlmChatApis

from .._private.ollama_chat import OllamaLlmChat



class LlmChatFactory:
	"""
		Represents a factory for each `ILlmChat`
	"""
		
	
	@classmethod
	def create(
			cls,
			chat_apis: ELlmChatApis
	) -> ILlmChat:
		"""
			Instantiates a chat associated with the specified APIs
            
            Parameters
            ----------
                chat_apis: ELlmChatApis
                    An `ELlmChatApis` value representing the APIs associated with the `ILlmChat` object
					for which instantiation is requested
            
            Returns
            -------
                ILlmChat
                    An `ILlmChat` object that allows you to manage a message chat specific to the
                    requested APIs
		"""
		obj: ILlmChat
		match chat_apis:
			case ELlmChatApis.OLLAMA:
				obj = OllamaLlmChat()
		
		return obj
	
		
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================