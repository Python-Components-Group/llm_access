class ChatNeverSelectedError(Exception):
	"""
		Represents a (non-exiting) exception that occurs when
		an operation is called without ever having set
		the required chat object
	"""
	pass