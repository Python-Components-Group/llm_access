from abc import abstractmethod
from .. import ILlmChat



class IMixedLlmChat(ILlmChat):
	"""
		Represents an `ILlmChat` that can also contain messages related to a tool's response.
        
        The compatible LLM APIs are specified by the descendants of this interface.
	"""


	@abstractmethod
	def add_tool_response(
			self,
			tool_response: str
	):
		"""
			Adds a response message to this chat, provided by a tool called by the LLM
            
            Parameters
            ----------
				tool_response: str
                    A string, single-line or multi-line, containing the response message
                    provided by a tool called by the LLM
					
			Raises
            ------
                ValueError
                    Occurs if:
                    
                        - The `tool_response` parameter is `None`
                        - The `tool_response` parameter is an empty string
		"""
		pass