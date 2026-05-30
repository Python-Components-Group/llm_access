class IncompatibleApiError(Exception):
	"""
		Represents a (non-exiting) exception that occurs when a provided object,
		associated with one or more APIs, is not compatible with the API
        associated with the object that throws this exception
	"""
	pass