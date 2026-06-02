from ..a_ollama_specimpl import AOllamaLlmSpecImpl



class Ollama_DeepseekCoder_33b_q4_0_LlmImpl(AOllamaLlmSpecImpl):
	"""
		Represents an `AOllamaLlmSpecImpl` for the "Deepseek-Coder-33B-q4_0" model
	"""
	
	def __init__(self):
		"""
			Creates a new Ollama_DeepseekCoder_33b_q4_0_LlmImpl
		"""
		super().__init__()
	
	
	def model_name(self) -> str:
		return "deepseek-coder:33b"
	
	
	def context_window(self) -> int:
		return 16384


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================