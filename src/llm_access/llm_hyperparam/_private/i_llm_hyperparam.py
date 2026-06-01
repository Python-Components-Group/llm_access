from typing import Any
from abc import ABC, abstractmethod

from ..id import ILlmHyperParamId



class ILlmHyperParam(ABC):
	"""
		Represents a specific hyperparameter of one or more LLMs.

        Each specific hyperparameter is associated with a single hyperparameter identifier.

		The represented parameter and its semantics are described by the chosen identifier
        and made known to the user by the descendants of this interface.
        The models and/or specific APIs to which the specific parameter belongs are described
        by the chosen identifier and made known to the user by the descendants
        of this interface.
	"""


	@abstractmethod
	def param_id(self) -> ILlmHyperParamId:
		"""
			Returns the identifier of the hyperparameter represented

            Returns
            -------
                ILlmHyperParamId
                    An `ILlmHyperParamId` object representing the identifier
                    of the hyperparameter
		"""
		pass


	@abstractmethod
	def set_value(self, value: str):
		"""
			Sets the value provided as an argument as the value for the LLM-specific
			hyperparameter represented by this ILlmHyperParam.
			
            Parameters
            ----------
				value: str
                    A string containing the value to set for this ILlmHyperParam
			
            Raises
            ------
                ValueError
                    Occurs if:
					
						- The `value` parameter is `None`
                        - The `value` parameter is an empty string
                        - The `value` parameter contains an invalid value for the
                          hyperparameter represented
		"""
		pass
	
	
	@abstractmethod
	def to_effvalue(self) -> Any:
		"""
			Returns the value of this LLM-specific hyperparameter in the actual type
            used by the API
            
            Returns
            -------
				Any
                    A value representing the last value set for this hyperparameter
                    in the type accepted by the specific API to which this LLMHyperParam is bound
		"""
		pass