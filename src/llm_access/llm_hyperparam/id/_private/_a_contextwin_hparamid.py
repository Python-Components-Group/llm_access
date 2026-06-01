from abc import abstractmethod
from ._a_base_hparamid import _ABaseHyperParamId



class _AContextWindowHyperParamId(_ABaseHyperParamId):
	"""
		Represents an `ILlmHyperParamId` that describes the hyperparameter
		of the context window.
		
		Each "Context Window" hyperparameter is named "context_name".
        
        The models and/or API specifications to which the specific hyperparameter belongs are described
        by the descendants of this abstract class
	"""
	
	
	def name(self) -> str:
		return "context_window"
	
	
	##	============================================================
	##						ABSTRACT METHODS
	##	============================================================

	
	@abstractmethod
	def id(self) -> str:
		pass
	
	
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================