from typing import Set
from abc import ABC, abstractmethod

from ...llm_api import ILlmApi
from ...llm_hyperparam.id import ILlmHyperParamId



class ILlmSpecImpl(ABC):
	"""
		Represents a specific implementation of an LLM, with any specific hyperparameters defined,
        linked to one or more specific APIs that enable interaction with it.
        
        Each ILlmSpecImpl is immutable.

		Each specific feature of the implementation is described by the descendants of this interface.
        The APIs to which the specific implementation is linked are described by the descendants
        of this interface. If there are multiple APIs, they must agree on every specific feature
        of the model implementation in order for this ILlmSpecImpl to be valid.
	"""


	@abstractmethod
	def model_name(self) -> str:
		"""
			Returns the model name, including the specific variant, which is associated with
			the specific implementation represented.
            The returned model name conforms to the format of the specific APIs described by
            the descendants of this interface.
            
            Returns
            -------
				str
                    A single-line string containing the model name of the specific
                    implementation represented by this ILlmSpecImpl.
                    This is the model identifier used by the specific APIs
		"""
		pass


	@abstractmethod
	def model_hyperparams(self) -> Set[ILlmHyperParamId]:
		"""
			Returns the model-specific parameters that can be used with this specific
			implementation.
			
			Returns
			-------
				Set[ILlmHyperParamId]
                    A set of `ILlmHyperParamId` objects representing the list of hyperparameters
                    that can be used in this specific implementation of the LLM
		"""
		pass


	@abstractmethod
	def context_window(self) -> int:
		"""
			Restituisce la massima finestra di contesto (numero di tokens massimi fornibili),
			durante l'interazione, con il modello descritto in questa specifica implementazione.
			Il numero di tokens è relativo all' intera chat di messaggi.

			Returns
			-------
				int
					Un intero indicante il numero di tokens massimi fornibili durante l'interazione
					con il modello descritto da questa specifica implementazione
		"""
		pass
	
	
	@abstractmethod
	def compat_apis(self) -> Set[ILlmApi]:
		"""
			Returns the set of LLM APIs that are compatible with this ILlmSpecImpl
            
            Returns
            -------
				Set[ILlmApi]
                    A set of `ILlmApi` objects representing the set of identifiers
                    of APIs with which this specific implementation of an LLM is compatible
		"""
		pass