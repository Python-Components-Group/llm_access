from typing import List, Dict, Set, Any
from .. import ILlmChat

from ...llm_api import (
	ILlmApi,
	OllamaApi
)

from ..exceptions import (
	ChatEmptyError,
	ChatNotEmptyError
)



class OllamaLlmChat(ILlmChat):
	"""
		Represents an `ILlmChat` that is bound to the LLMs API named "Ollama".
        
        The data type accepted by "Ollama" is a `List[Dict[str, str]]`, as specified
        in its documentation.
	"""
	
	def __init__(self):
		"""
			Builds a new OllamaLlmChat
		"""
		self._history: List[Dict[str, str]] = []
		
		
	def compat_apis(self) -> Set[ILlmApi]:
		return {OllamaApi()}
	
	
	def clear(self):
		self._history.clear()
	
	
	def set_system_prompt(self, sys_prompt: str):
		if len(self._history) != 0:
			raise ChatNotEmptyError()
		
		self._history[0] = {
			"role": "system",
			"content": sys_prompt
		}
	
	
	def add_prompt(self, user_prompt: str):
		if (user_prompt is None) or (user_prompt == ""):
			raise ValueError()
		
		self._history.append(
			{
				"role": "user",
				"content": user_prompt
			}
		)
	
	
	def add_response(self, response: str):
		if (response is None) or (response == ""):
			raise ValueError()
		
		self._history.append(
			{
				"role": "assistant",
				"content": response
			}
		)
	
	
	def get_last_prompt(self) -> str:
		if len(self._history) == 0:
			raise ChatEmptyError()
		
		return self._get_last_by_role("user")
	
	
	def get_last_response(self) -> str:
		if len(self._history) == 0:
			raise ChatEmptyError()
		
		return self._get_last_by_role("assistant")
	
	
	def chat_messages(self) -> Any:
		"""
			Returns the chat with the technology required for use by
            "Ollama"
            
            Returns
            -------
				List[Dict[str, str]]
                    A list of string dictionaries, indexed by strings, representing the chat messages
                    added after the last `.clear()`
		"""
		return self._history


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================


	def _get_last_by_role(self, role: str):
		i: int = len(self._history) - 1
		
		while (i >= 0):
			if self._history[i]["role"] == role:
				return self._history[i]["content"]
			i -= 1
		return ""