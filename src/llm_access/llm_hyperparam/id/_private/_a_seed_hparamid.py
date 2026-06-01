from abc import abstractmethod
from ._a_base_hparamid import _ABaseHyperParamId



class _ASeedHyperParamId(_ABaseHyperParamId):
	"""
		Represents an `ILlmHyperParamId` that describes the hyperparameter
		of the generation seed.
		
		Each "Generation Seed" hyperparameter is named "gen_seed".
        
        The models and/or API specifications to which the specific hyperparameter belongs are described
        by the descendants of this abstract class
	"""
	
	
	def name(self) -> str:
		return "gen_seed"
	
	
	##	============================================================
	##						ABSTRACT METHODS
	##	============================================================

	
	@abstractmethod
	def id(self) -> str:
		pass
	
	
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================