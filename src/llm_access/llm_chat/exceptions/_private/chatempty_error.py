class ChatEmptyError(Exception):
	"""
		Represents a (non-exiting) exception that occurs when
		an operation is performed without any messages in the
		chat in question
	"""
	pass