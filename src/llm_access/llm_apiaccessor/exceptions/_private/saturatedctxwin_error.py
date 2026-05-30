class SaturatedContextWindowError(Exception):
	"""
		Represents a (non-exiting) exception that occurs if the LLM,
		which has been asked to generate or correct a partial test suite,
		fills up the context window.
        This may be related to the issue of "Semantic Drifting."
	"""
	pass

