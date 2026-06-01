from .._a_topp_hparamid import _ATopPHyperParamId



class OllamaTopPHyperParamId(_ATopPHyperParamId):
	"""
		Represents an `ILlmHyperParamId` for each LLM to interact with
        via the "Ollama" platform.
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaTopPHyperParamId
		"""
		pass
	
	
	def id(self) -> str:
		return "top_p"


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================