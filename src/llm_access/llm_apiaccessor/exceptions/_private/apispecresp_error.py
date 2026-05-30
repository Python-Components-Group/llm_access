class ApiResponseError(Exception):
	"""
	    Represents a (non-exiting) exception that occurs when an error occurs
	    regarding the API chosen for interaction during the response to a
	    request made to an LLM.
        The nature of the error may be unspecified.
	    
	    The `args` attribute is set to the `args` value of the specific exception
        that occurred with the API (if it can be obtained).
	    Anything added is specified by the provider/creator of the object.
	"""
	pass