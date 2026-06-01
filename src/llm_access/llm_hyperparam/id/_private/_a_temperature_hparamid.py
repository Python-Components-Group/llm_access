from abc import abstractmethod
from ._a_base_hparamid import _ABaseHyperParamId



class _ATemperatureHyperParamId(_ABaseHyperParamId):
	"""
		Represents an `ILlmHyperParamId` that describes the temperature hyperparameter.
		
		Each "Temperature" hyperparameter is named "temperature".
        
        The models and/or API specifications to which the specific hyperparameter belongs are described
        by the descendants of this abstract class
	"""
	
	
	def name(self) -> str:
		return "temperature"
	
	
	##	============================================================
	##						ABSTRACT METHODS
	##	============================================================

	
	@abstractmethod
	def id(self) -> str:
		pass
	
	
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================