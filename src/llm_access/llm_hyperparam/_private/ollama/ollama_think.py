from typing import Any
from .._a_base_llmhyperparam import _ABaseLlmHyperparam

from ...id import ILlmHyperParamId
from ...id._private.ollama.ollama_think_id import OllamaThinkHyperParamId



class OllamaThinkHyperParam(_ABaseLlmHyperparam):
	"""
		Represents an `ILlmHyperParam` for the "think" hyperparameter for each
        LLM to be interacted with via the "Ollama" platform.
        
        The hyperparameter's value type is `bool`
	"""
	
	def __init__(self):
		"""
			Creates a new OllamaThinkHyperParam
		"""
		super().__init__()
		
		
	def _ap__param_id(self) -> ILlmHyperParamId:
		return OllamaThinkHyperParamId()
	
	
	def _ap__default_value(self) -> str:
		return "False"
	
	
	def _ap__assert_semvalidity(
			self,
			value: str
	):
		value_str: str = value.capitalize()
		if (value_str != "True") and (value_str != "False"):
			raise ValueError()
		
		
	def to_effvalue(self) -> Any:
		value_str: str = self._p__get_str_value().capitalize()
		if value_str != "True":
			value_str = ""
		return bool(value_str)


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================