class ChatNotEmptyError(Exception):
	"""
		Represents a (non-exiting) exception that occurs when
		an operation is performed while the chat in question
		is not empty
	"""
	pass