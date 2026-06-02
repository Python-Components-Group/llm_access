from .._a_wantsthinking_hparamid import _AWantsThinkingHyperParamId



class OllamaThinkHyperParamId(_AWantsThinkingHyperParamId):
	"""
		Represents an `AWantsThinkingHyperParamId` for each LLM to interact with
        via the "Ollama" platform.
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaThinkHyperParamId
		"""
		super().__init__()
	
	
	def id(self) -> str:
		return "think"


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================