from typing import Any
from .._a_base_llmhyperparam import _ABaseLlmHyperparam

from ...id import ILlmHyperParamId
from ...id._private.ollama.ollama_topk_id import OllamaTopKHyperParamId



class OllamaTopKHyperParam(_ABaseLlmHyperparam):
	"""
		Represents an `ILlmHyperParam` for the "top-k" hyperparameter for each
        LLM to be interacted with via the "Ollama" platform.
        
        The data type for the hyperparameter is `int`.
        Additionally, the following condition must be met: `value >= 0`
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaTopKHyperParam
		"""
		super().__init__()
	
	
	def _ap__param_id(self) -> ILlmHyperParamId:
		return OllamaTopKHyperParamId()
	
	
	def _ap__default_value(self) -> str:
		return "40"
	
	
	def _ap__assert_semvalidity(self, value: str):
		topk: int = int(value)
		if topk < 0:
			raise ValueError()
	
	
	def to_effvalue(self) -> Any:
		return int(self._p__get_str_value())


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================