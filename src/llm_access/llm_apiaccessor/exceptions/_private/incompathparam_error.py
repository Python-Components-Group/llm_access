class IncompatibleHyperparamError(Exception):
	"""
		Represents a (non-exiting) exception that occurs when an attempt
		is made to set a hyperparameter that is incompatible with the
		specific implementation of the selected LLM
	"""
	pass