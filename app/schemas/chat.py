from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=32768)
    max_tokens: int = Field(default=1000, ge=1, le=32768)

class ChatResponse(BaseModel):
    completion: str