from ... import ILlmHyperParamId



class OllamaNumPredictHyperParamId(ILlmHyperParamId):
	"""
		Represents an `ILlmHyperParamId` for the "num_predict" hyperparameter for each
        LLM to be interacted with via the "Ollama" platform.
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaNumPredictHyperParam
		"""
		pass
	
	
	def name(self) -> str:
		return "num_predict"
	
	
	def id(self) -> str:
		return "num_predict"


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================