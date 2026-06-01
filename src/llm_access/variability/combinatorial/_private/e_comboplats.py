from enum import (
	Enum as PythonEnumerator,
	auto
)



class EPlatformCombo(PythonEnumerator):
	"""
		Represents a combination of one or more inference platforms supported by
        the "llm_access" component and compatible with one another in terms of
        certain features
	"""
	OLLAMA = auto(),