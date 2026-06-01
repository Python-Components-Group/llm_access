from enum import (
	Enum as PythonEnumerator,
)



class EModelPlatformCombo(PythonEnumerator):
	"""
		Represents a combination of one or more inference platforms and one or more LLMs,
        supported by "llm_access" component and compatible with one another in terms of
        certain characteristics
	"""
	# Currently, there are no platforms that are compatible with each other, nor are there
	# any models for which entries are required in this enumeration list
    
    # First, list the platforms, separated by the character "_"
    # Then, list the models, separated by the character "_"
    # Platforms and models are separated by the string "__"
	pass