from typing import Any
from .._a_base_llmhyperparam import _ABaseLlmHyperparam

from ...id import ILlmHyperParamId
from ...id._private.ollama.ollama_numgpu_id import OllamaNumGpuHyperParamId



class OllamaNumGpuHyperParam(_ABaseLlmHyperparam):
	"""
		Represents an `ILlmHyperParam` for the "num_gpu" hyperparameter for each
        LLM to be interacted with via the "Ollama" platform.
        
        The data type for this hyperparameter is `int`.
        Additionally, the following condition must be met: `value >= 0`.
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaNumGpuHyperParam
		"""
		super().__init__()
	
	
	def _ap__param_id(self) -> ILlmHyperParamId:
		return OllamaNumGpuHyperParamId()
	
	
	def _ap__default_value(self) -> str:
		return "0"
	
	
	def _ap__assert_semvalidity(self, value: str):
		value_int: int = int(value)
		if value_int < 0:
			raise ValueError()
		
		
	def to_effvalue(self) -> Any:
		return int(self._p__get_str_value())


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================