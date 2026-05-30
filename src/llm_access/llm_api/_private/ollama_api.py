from ._a_base_llmapi import _ABaseLlmApi



class OllamaApi(_ABaseLlmApi):
	"""
		Represents an `ILlmApi` to identify the "Ollama" API
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaApi
		"""
		pass
	
	
	def api_name(self) -> str:
		return "ollama"


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================