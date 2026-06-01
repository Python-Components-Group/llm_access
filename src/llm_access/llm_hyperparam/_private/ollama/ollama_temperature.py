from typing import Any
from .._a_base_llmhyperparam import _ABaseLlmHyperparam

from ...id import ILlmHyperParamId
from ...id._private.ollama.ollama_temperature_id import OllamaTemperatureHyperParamId



class OllamaTemperatureHyperParam(_ABaseLlmHyperparam):
	"""
		Represents an `ILlmHyperParam` for the "temperature" hyperparameter for each
        LLM to be interacted with via the "Ollama" platform.
        
        The data type for the hyperparameter is `float`.
        Additionally, the following condition must be met: `0.0 <= value <= 1.0`
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaTemperatureHyperParam
		"""
		super().__init__()
	
	
	def _ap__param_id(self) -> ILlmHyperParamId:
		return OllamaTemperatureHyperParamId()
	
	
	def _ap__default_value(self) -> str:
		return "0.5"
	
	
	def _ap__assert_semvalidity(self, value: str):
		temp: float = float(value)
		if (temp < 0.0) or (temp > 1.0):
			raise ValueError()
	
	
	def to_effvalue(self) -> float:
		return float(self._p__get_str_value())


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================