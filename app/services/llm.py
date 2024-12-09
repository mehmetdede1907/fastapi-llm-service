# app/services/llm.py
from anthropic import Anthropic
from app.core.config import get_settings
from app.core.logging import setup_logging

logger = setup_logging()
settings = get_settings()

class LLMService:
    def __init__(self):
        self.client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    
    async def get_completion(self, prompt: str, max_tokens: int = 1000):
        """Get completion from Claude with telemetry tracking"""
        try:
            logger.info(f"Sending request to Claude with prompt length: {len(prompt)}")
            
            # Create the message - remove await
            response = self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=max_tokens,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            
            # Extract the response text and ensure it's a string
            completion_text = str(response.content[0].text)
            
            logger.info(f"Received response from Claude")
            return completion_text
            
        except Exception as e:
            logger.error(f"Error in LLM service: {str(e)}")
            raise