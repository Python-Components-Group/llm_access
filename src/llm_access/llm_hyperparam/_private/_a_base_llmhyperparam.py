from abc import abstractmethod
from .. import ILlmHyperParam

from ..id import ILlmHyperParamId



class _ABaseLlmHyperparam(ILlmHyperParam):
	"""
		Represents a base `ILlmHyperParam`, meaning it contains the control logic
        common to every `ILlmHyperParam`.
        
		The represented parameter and its semantics are described by the chosen identifier
        and made known to the user by the descendants of this interface.
        The models and/or specific APIs to which the specific parameter belongs are described
        by the chosen identifier and made known to the user by the descendants
        of this interface.
	"""
	
	def __init__(self):
		"""
			Creates a new _ABaseLlmHyperparam
		"""
		self._id: ILlmHyperParamId = self._ap__param_id()
		self._value: str = self._ap__default_value()
	
	
	def param_id(self) -> ILlmHyperParamId:
		return self._id
	
	
	def set_value(self, value: str):
		if (value is None) or (value == ""):
			raise ValueError()
		
		self._ap__assert_semvalidity(value)
		
		self._value = value
		
	
	##	============================================================
	##						ABSTRACT METHODS
	##	============================================================
	
	
	@abstractmethod
	def _ap__param_id(self) -> ILlmHyperParamId:
		"""
			Returns the identifier of the hyperparameter associated with the
            hyperparameter represented
            
            Returns
            -------
				ILlmHyperParamId
                    An `ILlmHyperParamId` object representing the identifier associated
                    with this hyperparameter
		"""
		pass
	
	
	@abstractmethod
	def _ap__default_value(self) -> str:
		"""
			Returns the default value for the hyperparameter represented
            
            Returns
            -------
				str
                    A string representing the default value for the hyperparameter
                    represented.
                    The default value does not necessarily have to be valid for the
                    hyperparameter. It may also be an invalid initialization
                    for its semantics
		"""
		pass
	
	
	@abstractmethod
	def _ap__assert_semvalidity(self, value: str):
		"""
			Checks the semantic validity of the value provided for the
			hyperparameter represented.
            
            If the check succeeds, this operation is equivalent to a no-op
            
            Parameters
            ----------
				value: str
                    A string representing the value of the hyperparameter to be verified
                    
            Raises
            ------
                ValueError
                    Occurs if the value parameter contains an invalid value for
                    the represented hyperparameter
		"""
		pass
	
	
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================


	def _p__get_str_value(self) -> str:
		"""
			Returns the value, as a string, currently assigned to the
            represented hyperparameter
            
            Returns
            -------
                str
                    A string representing the value currently assigned to the
                    represented hyperparameter
		"""
		return self._value