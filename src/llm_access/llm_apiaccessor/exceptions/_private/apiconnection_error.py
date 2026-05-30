class ApiConnectionError(ConnectionError):
	"""
		Represents a (non-exiting) exception that occurs when an error
		occurs during an attempt to connect to an LLM API.
        
        The `args` attribute is set to the `args` value of the specific
        exception that occurred with the API (if it can be obtained).
        Anything added is specified by the provider/creator of the object.
	    
	    The `errno` attribute is set to the `errno` value of the
        `ConnectionError` that occurred with the API (if it can be obtained).
        Anything added is specified by the provider/creator of the object.
	"""
	pass