from .._a_topk_hparamid import _ATopKHyperParamId



class OllamaTopKHyperParamId(_ATopKHyperParamId):
	"""
		Represents an `ATopKHyperParamId` for each LLM to interact with
        via the "Ollama" platform.
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaTopKHyperParamId
		"""
		pass
	
	
	def id(self) -> str:
		return "top_k"


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================