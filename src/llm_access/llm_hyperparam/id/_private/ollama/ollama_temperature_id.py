from .._a_temperature_hparamid import _ATemperatureHyperParamId



class OllamaTemperatureHyperParamId(_ATemperatureHyperParamId):
	"""
		Represents an `ATemperatureHyperParamId` for each LLM to interact with
        via the "Ollama" platform.
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaTemperatureHyperParamId
		"""
		pass
	
	
	def id(self) -> str:
		return "temperature"


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================