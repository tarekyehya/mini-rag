from .providers import CoHereProvider, OpenAIProvider
from .LLMEnums import LLMEnums

class LLMProviderFactory:
    def __init__(self, config: dict):
        self.config = config
    
    def create(self, provider: str):
        if provider == LLMEnums.OPENAI:
            return OpenAIProvider(
                api_key = self.config.OPENAI_API_KEY,
                api_url = self.config.OPENAI_API_URL,
                default_input_max_chars = self.config.INPUT_DAFAULT_MAX_CHARACTERS,
                default_generation_max_output_tokens = self.config.GENERATION_DAFAULT_MAX_TOKENS,
                temperature = self.config.GENERATION_DAFAULT_TEMPERATURE
            )
        if provider == LLMEnums.COHERE:
            return CoHereProvider(
                api_key = self.config.COHERE_API_KEY,
                default_input_max_chars = self.config.INPUT_DAFAULT_MAX_CHARACTERS,
                default_generation_max_output_tokens = self.config.GENERATION_DAFAULT_MAX_TOKENS,
                temperature = self.config.GENERATION_DAFAULT_TEMPERATURE
            )
            
 
        
        return None
        
    
    
    