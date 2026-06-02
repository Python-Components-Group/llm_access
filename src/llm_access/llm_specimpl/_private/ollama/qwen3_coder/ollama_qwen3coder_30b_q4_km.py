from ..a_ollama_specimpl import AOllamaLlmSpecImpl



class Ollama_Qwen3Coder_30b_q4_km_LlmImpl(AOllamaLlmSpecImpl):
	"""
		Represents an `AOllamaLlmSpecImpl` for the "Qwen3-Coder-30B-q4_K_M" model
	"""
	
	def __init__(self):
		"""
			Creates a new Ollama_Qwen3Coder_30b_q4_km_LlmImpl
		"""
		super().__init__()
	
	
	def model_name(self) -> str:
		return "qwen3-coder:30b"

	
	def context_window(self) -> int:
		return 262144


	##	============================================================
	##						PRIVATE METHODS
	##	============================================================