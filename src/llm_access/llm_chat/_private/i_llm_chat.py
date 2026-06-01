from typing import Set, Any
from abc import ABC, abstractmethod

from ...llm_api import ILlmApi



class ILlmChat(ABC):
	"""
		Represents a chat between a user and a Large Language Model that is bound
		to one or more Large Language Model APIs.
        
        This object is capable of returning the chat in the type and format
        accepted by the LLM APIs linked to this ILlmChat.
		
		The compatible LLM APIs are specified by the descendants of this interface.
        The data type and format accepted by the APIs are specified by the descendants of
        this interface. In the case of multiple APIs, they must match in the data type
        and format of the chat they use
	"""
	
	
	@abstractmethod
	def compat_apis(self) -> Set[ILlmApi]:
		"""
			Returns the set of LLM APIs that are compatible with this ILlmChat

			Returns
			-------
				Set[ILlmApi]
                    A set of `ILlmApi` objects representing the set of identifiers
                    of APIs with which this chat is compatible
		"""
		pass


	@abstractmethod
	def clear(self):
		"""
			Reset the chat to its initial state, as if it had just been created
		"""
		pass
	
	
	@abstractmethod
	def set_system_prompt(self, sys_prompt: str):
		"""
			Set the "System Prompt" (or "Context Prompt") for this chat
            
            Parameters
            ----------
                sys_prompt: str
					A string, single-line or multi-line, containing the
					"System Prompt" to contextualize this chat
            
            Raises
            ------
                ChatNotEmptyError
                    Occurs if the chat already contains at least one message
		"""
		pass
	
	
	@abstractmethod
	def add_prompt(self, user_prompt: str):
		"""
			Adds a prompt message provided by the user to this chat
            
            Parameters
            ----------
                user_prompt: str
                    A string (single-line or multi-line) containing the
                    user's prompt message
					
			Raises
            ------
                ValueError
                    Occurs if:
                    
                        - The `user_prompt` parameter is `None`
                        - The `user_prompt` parameter is an empty string
		"""
		pass
	
	
	@abstractmethod
	def add_response(self, response: str):
		"""
			Records a response message, provided by the LLM, in this chat
            
            Parameters
            ----------
                response: str
                    A string, either single-line or multi-line, containing
                    the response message from the Large Language Model
					
			Raises
            ------
                ValueError
                    Occurs if:
                    
                        - The `response` parameter is `None`
                        - The `response` parameter is an empty string
		"""
		pass
	
	
	@abstractmethod
	def get_last_prompt(self) -> str:
		"""
			Returns the last prompt in this chat.
            
            Returns
            -------
                str
                    A string containing the last prompt in this chat
		"""
		pass
	
	
	@abstractmethod
	def get_last_response(self) -> str:
		"""
			Returns the LLM's latest response from this chat.
            
            Returns
            -------
                str
                    A string containing the LLM's latest response
                    from this chat
		"""
		pass
	
	
	@abstractmethod
	def chat_messages(self) -> Any:
		"""
			Returns the chat with the technology required for its use by the
            specific APIs
            
            Returns
            -------
                Any
					A potential object representing the chat of added messages, after the last
					`.clear()`, represented by the implementation technology required by the
					specific APIs to which this `ILlmChat` is bound.
                    The type corresponding to the required technology is specified by the descendants
                    of this interface.
		"""
		pass