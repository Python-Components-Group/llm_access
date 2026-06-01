from typing import Any
from .._a_base_llmhyperparam import _ABaseLlmHyperparam

from ...id import ILlmHyperParamId
from ...id._private.ollama.ollama_topp_id import OllamaTopPHyperParamId



class OllamaTopPHyperParam(_ABaseLlmHyperparam):
	"""
		Represents an `ILlmHyperParam` for the "top-p" hyperparameter for each
        LLM to be interacted with via the "Ollama" platform.
        
        The data type for the hyperparameter is `float`.
        Additionally, the following condition must be met: `0.0 <= value <= 1.0`
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaTopPHyperParam
		"""
		super().__init__()
	
	
	def _ap__param_id(self) -> ILlmHyperParamId:
		return OllamaTopPHyperParamId()
	
	
	def _ap__default_value(self) -> str:
		return "0.9"
	
	
	def _ap__assert_semvalidity(self, value: str):
		topp: float = float(value)
		if (topp < 0.0) or (topp > 1.0):
			raise ValueError()
	
	
	def to_effvalue(self) -> Any:
		return float(self._p__get_str_value())


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================