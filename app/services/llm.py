from anthropic import Anthropic
from app.core.config import get_settings
from app.core.logging import setup_logging

logger = setup_logging()
settings = get_settings()

class LLMService:
    def __init__(self):
        self.client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    
    async def get_completion(self, prompt: str, max_tokens: int = 1000):
        try:
            logger.info(f"Sending request to Claude with prompt length: {len(prompt)}")
            
            response = await self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=max_tokens,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            
            logger.info(f"Received response from Claude with {response.usage.total_tokens} tokens")
            return response.content[0].text
            
        except Exception as e:
            logger.error(f"Error in LLM service: {str(e)}")
            raise