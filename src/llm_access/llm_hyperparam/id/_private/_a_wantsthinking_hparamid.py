from abc import abstractmethod
from ._a_base_hparamid import _ABaseHyperParamId



class _AWantsThinkingHyperParamId(_ABaseHyperParamId):
	"""
		Represents an `ILlmHyperParamId` that describes the hyperparameter
        "Thinking required".
		
		Every "Thinking required" hyperparameter has the name "think".
        
        The models and/or API specifications to which the specific hyperparameter belongs are described
        by the descendants of this abstract class
	"""
	
	
	def name(self) -> str:
		return "think"
	
	
	##	============================================================
	##						ABSTRACT METHODS
	##	============================================================

	
	@abstractmethod
	def id(self) -> str:
		pass
	
	
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================