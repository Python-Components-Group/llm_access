from .._a_seed_hparamid import _ASeedHyperParamId



class OllamaSeedHyperParamId(_ASeedHyperParamId):
	"""
		Represents an `ASeedHyperParamId` for each LLM to interact with
        via the "Ollama" platform.
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaSeedHyperParamId
		"""
		super().__init__()
	
	
	def id(self) -> str:
		return "seed"


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================