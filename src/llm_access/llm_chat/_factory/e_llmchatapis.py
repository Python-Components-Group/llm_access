from enum import Enum as PythonEnumerator



class ELlmChatApis(PythonEnumerator):
	"""
		Represents a strategy for selecting `ILlmChat` objects, based on the APIs
        to which the concrete instance is required to be bound.
	"""
	OLLAMA = 0,