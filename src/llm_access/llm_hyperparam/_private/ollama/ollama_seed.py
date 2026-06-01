from typing import Any
from .._a_base_llmhyperparam import _ABaseLlmHyperparam

from ...id import ILlmHyperParamId
from ...id._private.ollama.ollama_seed_id import OllamaSeedHyperParamId



class OllamaSeedHyperParam(_ABaseLlmHyperparam):
	"""
		Represents an `ILlmHyperParam` for the "seed" hyperparameter for each
        LLM with which to interact via the "Ollama" platform.
        
        The data type for the hyperparameter is `int`.
        Additionally, the following condition must be met: `value >= -1`.
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaSeedHyperParam
		"""
		super().__init__()
	
	
	def _ap__param_id(self) -> ILlmHyperParamId:
		return OllamaSeedHyperParamId()
	
	
	def _ap__default_value(self) -> str:
		return "-1"
	
	
	def _ap__assert_semvalidity(self, value: str):
		seed :int = int(value)
		if seed < -1:
			raise ValueError()
	
	
	def to_effvalue(self) -> Any:
		return int(self._p__get_str_value())


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================