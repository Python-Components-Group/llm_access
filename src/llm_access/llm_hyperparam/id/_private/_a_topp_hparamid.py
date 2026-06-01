from abc import abstractmethod
from ._a_base_hparamid import _ABaseHyperParamId



class _ATopPHyperParamId(_ABaseHyperParamId):
	"""
		Represents an `ILlmHyperParamId` that describes the hyperparameter
        top-p.
		
		Every "Top-P" hyperparameter is named "top-p".
        
        The models and/or API specifications to which the specific hyperparameter belongs are described
        by the descendants of this abstract class
	"""
	
	
	def name(self) -> str:
		return "top-p"
	
	
	##	============================================================
	##						ABSTRACT METHODS
	##	============================================================

	
	@abstractmethod
	def id(self) -> str:
		pass
	
	
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================