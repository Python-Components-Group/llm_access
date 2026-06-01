from enum import (
	Enum as PythonEnumerator,
	auto
)



class EModelCombo(PythonEnumerator):
	"""
		Represents a combination of one or more Large Language Models supported by the
		"llm_access" component that are compatible with one another in terms of certain
		characteristics
	"""
	QWEN3_32B_Q4_K_M = auto(),
	DEEPSEEK_CODER_33B_Q4_0 = auto()