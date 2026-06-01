from ... import ILlmHyperParamId



class OllamaNumGpuHyperParamId(ILlmHyperParamId):
	"""
		Represents an `ILlmHyperParamId` for the "num_gpu" hyperparameter for each
        LLM to be interacted with via the "Ollama" platform.
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaNumGpuHyperParamId
		"""
		pass
	
	
	def name(self) -> str:
		return "num_gpu"
	
	
	def id(self) -> str:
		return "num_gpu"


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================