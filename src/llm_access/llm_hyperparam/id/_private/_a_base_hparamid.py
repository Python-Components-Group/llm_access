from abc import abstractmethod
from .. import ILlmHyperParamId



class _ABaseHyperParamId(ILlmHyperParamId):
	"""
		It represents a base `ILlmHyperParamId`, meaning it contains the logic
        common to every `ILlmHyperParamId`
		
		The hyperparameter represented and its semantics are described by the descendants of this
		abstract class.
        The models and/or specific APIs to which the hyperparameter belongs are described by the
        descendants of this abstract class.
	"""
	
	def __init__(self):
		"""
			Creates a new _ABaseHyperParamId
		"""
		pass
	
	
	def __hash__(self):
		return hash(self.id())
		
		
	def __eq__(self, other):
		if not isinstance(other, ILlmHyperParamId):
			return False
		
		return self.id() == other.id()
	

	##	============================================================
	##						ABSTRACT METHODS
	##	============================================================
	
	
	@abstractmethod
	def name(self) -> str:
		pass
	
	
	@abstractmethod
	def id(self) -> str:
		pass
		
		
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================