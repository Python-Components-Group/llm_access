from typing import List

from .i_llm_hparam_f import ILlmHyperParamFactory
from ...variability.combinatorial import (
	EModelCombo, EPlatformCombo, EModelPlatformCombo
)

from .ollama_hparam_f import OllamaHyperParamFactory



class LlmHyperParamFactoryResolver:
	"""
		Represents a factory of `ILlmHyperParamFactory`
	"""
	
	
	@classmethod
	def resolve(
			cls,
	        models_apis: str
	) -> ILlmHyperParamFactory:
		"""
			Instantiates a new `ILlmHyperParamFactory` for the requested model/platform combination
            
            Parameters
            ----------
                models_apis: str
                    A string representing the models and/or platforms from which to obtain
					the hyperparameter factory.
                    If both models and platforms are specified, the string
                    is semicolon-separated between the two parts ("<models>;<apis>")
                    
            Returns
            -------
				ILlmHyperParamFactory
                    An `ILlmHyperParamFactory` object that allows you to instantiate hyperparameters
                    for the selected models/platforms requested
                    
            Raises
            ------
                ValueError
					Occurs if:
                        
                        - The `models_apis` parameter is `None`
                        - The `models_apis` parameter is an empty string
                        - The `models_apis` parameter, if it does not have 2 parts, does not represent
						  a valid combination of platforms or models;
                
                NotImplementedError
                    Occurs if the factory for the requested model/platform combination is not
                    currently implemented, or does not exist, in the "llm_access" component
		"""
		obj_f: ILlmHyperParamFactory
		
		parts: List[str] = models_apis.split(";")
		for i in range(0, len(parts)):
			parts[i]: str = parts[i].replace("-","_").replace(":", "_").lower().upper()
		
		if len(parts) == 2:
			obj_f = cls._create_llmsplat_factory(parts[0], parts[1])
		else:
			models_or_apis: str = models_apis.upper()
			try:
				platforms: EPlatformCombo = EPlatformCombo[models_or_apis]
				obj_f = cls._create_platonly_factory(platforms)
			except KeyError:
				try:
					models: EModelCombo = EModelCombo[models_or_apis]
					obj_f = cls._create_llmonly_factory(models)
				except KeyError:
					raise ValueError()
			
		return obj_f
		
		
	##	============================================================
	##						PRIVATE METHODS
	##	============================================================
	
	
	@classmethod
	def _create_llmsplat_factory(
			cls,
			models: str,
			apis: str
	) -> ILlmHyperParamFactory:
		try:
			models_apis_combo: EModelPlatformCombo = EModelPlatformCombo[
				"__".join([apis, models]).upper()
			]
		except KeyError:
			raise NotImplementedError()
		
		# Non ancora implementato, poichè non necessario attualmente
		match models_apis_combo:
			case None:
				pass
		
		return None


	@classmethod
	def _create_platonly_factory(
			cls,
			platforms: EPlatformCombo
	) -> ILlmHyperParamFactory:
		match platforms:
			case EPlatformCombo.OLLAMA:
				return OllamaHyperParamFactory()
	
	
	@classmethod
	def _create_llmonly_factory(
			cls,
			platforms: EModelCombo
	) -> ILlmHyperParamFactory:
		pass