from abc import ABC, abstractmethod

from ...llm_chat import ILlmChat
from ...llm_specimpl import ILlmSpecImpl
from ...llm_hyperparam import ILlmHyperParam



class ILlmApiAccessor(ABC):
	"""
		Represents an object that allows interaction with an LLM through the use of any API that provides LLMs.

		After creating an ILlmApiAccessor, you must execute the following operations:

			1- The `.set_chat(...)` operation ` to associate it with the chat to be used for requests (initially the first one)
			2- The `.select_model(...)` operation to select the first model with which interactions will take place

        The specific API to which each ILlmApiAccessor object is bound is described by the descendants of this interface.
	"""
		

	@abstractmethod
	def set_chat(
			self,
			chat: ILlmChat,
			erase_now: bool=True,
			erase_model: bool=True
	):
		"""
			Change the chat used for future interactions with LLMs using this ILlmApiAccessor.
			Optionally, you can choose not to delete the messages from the associated chat
            
            Parameters
            ----------
                chat: ILlmChat
					An `ILlmChat` object representing the new chat to be associated for the next interactions
                
                erase_now: bool
                    Optional. Default = `True`. A boolean indicating whether to delete all messages
                    from the new associated chat
					
				erase_model: bool
                    Optional. Default = `True`. A boolean indicating whether to delete all messages
                    from the new associated chat on every model change
					
			Raises
            ------
                ValueError
                    Occurs if the `chat` parameter is `None`
                    
                IncompatibleApiError
                    Occurs if none of the provided chat APIs are compatible
                    with the represented API
		"""
		pass


	@abstractmethod
	def select_model(self, model: ILlmSpecImpl):
		"""
			Select a new model with which this ILlmApiAccessor will perform all future interactions.
            
            If a model had already been selected and hyperparameters set, they are removed.
            
            Parameters
            ----------
				model: ILlmSpecImpl
                    An ILlmSpecImpl representing the specific LLM implementation to be used
                    for subsequent interactions.

			Raises
            ------
                ChatNeverSelectedError
                    Occurs if a chat object to be used has never been set
            
                ValueError
                    Occurs if `model` is None
					
				IncompatibleApiError
                    Occurs if the API represented by this ILlmApiAccessor is not compatible
                    with the APIs of the selected model
		"""
		pass


	@abstractmethod
	def add_hyperparam(self, hparam: ILlmHyperParam):
		"""
			Adds a new hyperparameter to be used in subsequent interactions

            Parameters
            ----------
                hparam: ILlmHyperParam
                    An `ILlmHyperParam` object representing the LLM-specific parameter
                    whose value is to be set

			Raises
            ------
                ChatNeverSelectedError
                    Occurs if a chat object to be used has never been set
            
                ModelNotSelectedError
                    Occurs if no model has been selected for this ILlmApiAccessor
			
				ValueError
                    Occurs if the `hparam` parameter has a value of `None`
                    
                IncompatibleHyperparamError
                    Occurs if the provided hyperparameter `hparam` is not acceptable
                    by the chosen LLM implementation
					
				HyperparamAlreadyExistsError
                    Occurs if the provided hyperparameter `hparam` has already been
                    added to this ILlmApiAccessor
		"""
		pass
	
	
	@abstractmethod
	def remove_hyperparam(self, hparam: ILlmHyperParam):
		"""
			Removes a previously added hyperparameter, for subsequent interactions

            Parameters
            ----------
                hparam: ILlmHyperParam
                    An `ILlmHyperParam` object representing the hyperparameter to remove

			Raises
            ------
                ChatNeverSelectedError
                    Occurs if a chat object to be used has never been set
            
                ModelNotSelectedError
                    Occurs if no model has been selected for this ILlmApiAccessor
			
				ValueError
                    Occurs if the `hparam` parameter has a value of `None`
                    
                HyperparamNotExistsError
                    Occurs if the provided hyperparameter `hparam` is not present among the
                    hyperparameters added to this ILlmApiAccessor
		"""
		pass


	@abstractmethod
	def prompt(self, timeout: int) -> str:
		"""
			Performs a single interaction with the selected model by providing it with last
            prompt registered in the chat

            Parameters
            ----------
				timeout: int
                    An integer representing the response timeout (in milliseconds) after which
                    the response is declared failed

            Returns
            -------
                str
                    A string containing the model's response to the interaction

			Raises
            ------
                ChatNeverSelectedError
                    Occurs if a chat object to use has never been set.
            
                ModelNotSelectedError
                    Occurs if no model has been selected for this ILlmApiAccessor.
					
				InvalidPromptError
                    Occurs if the request prompt is invalid for the represented API
                
                ApiConnectionError
                    Occurs if a connection error occurs with the inference platform.
                    The error belongs to its domain.
					The `args[0]` attribute, of type string, is used to distinguish the nature of the error:
                    
                        - "timeout": The error is related to a connection timeout
                        - "other": The error is of another type (as indicated by the other components of the `args` attribute)
				
				ResponseTimedOutError
                    Occurs if the specified `timeout` expires and no part of the response has been received
					
				ApiResponseError
                    Occurs if the request sent to the API produces a response error
                    belonging to its domain.
                    The `args[0]` attribute, of type string, is used to distinguish the nature of the error:
					
						- "known": The nature of the error is described by the inference platform
                        - "unknown": The nature of the error is not described by the inference platform and is unknown
                    
                SaturatedContextWindowError
                    Occurs if the context window becomes saturated during the interaction
		"""
		pass