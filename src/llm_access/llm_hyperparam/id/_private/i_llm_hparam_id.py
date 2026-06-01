from abc import ABC, abstractmethod



class ILlmHyperParamId(ABC):
	"""
		Represents an object that identifies a specific parameter (decoding/sampling parameter,
        or hyperparameter) of one or more LLMs.
        Each ILlmHyperParamId is immutable.
		
		Each ILlmHyperParamId is hashable (via `.__hash__(...)`) and comparable (via `.__eq__(...)`).
		
		Since the availability of an LLM’s hyperparameter depends on the specific model, the variant of
		the model being used, and the specific API that provides interaction with it; this interface allows
		these three factors to be modeled in an interrelated manner.

		If a specific parameter is associated with more than one specific LLM implementation it is mandatory
		that the semantics (meaning, format, name, and range of values) for both LLMs is identical.
		This is consistent with a similar approach taken for multiple specific APIs.
		
		For each identifier, there is only one implemented hyperparameter (i.e., one capable of
        valuation).
        
		The hyperparameter represented and its semantics are described by the descendants of this interface.
        The models and/or specific APIs to which the hyperparameter belongs are described by the descendants
        of this interface.
	"""


	@abstractmethod
	def name(self) -> str:
		"""
			Returns the name that describes the represented hyperparameter

            Returns
            -------
                str
                    A single-line string containing the name that describes the semantics
                    of the represented hyperparameter
		"""
		pass
	
	
	@abstractmethod
	def id(self) -> str:
		"""
			Returns the string identifier for the hyperparameter represented
            
            Returns
            -------
				str
                    A single-line string containing the identifier for the hyperparameter
                    represented relative to the models and/or API specifications to which
                    it belongs
		"""
		pass