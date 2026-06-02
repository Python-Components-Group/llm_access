from .._a_contextwin_hparamid import _AContextWindowHyperParamId



class OllamaNumCtxHyperParamId(_AContextWindowHyperParamId):
	"""
		Represents an `AContextWindowHyperParamId` for each LLM to interact with
        via the "Ollama" platform.
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaNumCtxHyperParamId
		"""
		super().__init__()
		
		
	def id(self) -> str:
		return "num_ctx"


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================