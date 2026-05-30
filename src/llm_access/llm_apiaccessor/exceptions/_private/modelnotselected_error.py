class ModelNotSelectedError(Exception):
	"""
		Represents a (non-exiting) exception that occurs when
		an operation is executed without first setting an LLM
		to use
	"""
	pass