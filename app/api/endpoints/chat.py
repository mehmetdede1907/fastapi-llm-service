# app/api/endpoints/chat.py
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.llm import LLMService
from app.api.dependencies import get_current_user
from app.core.logging import setup_logging

router = APIRouter()
logger = setup_logging()
llm_service = LLMService()

@router.post("/completion", response_model=ChatResponse)
async def get_completion(
    request: ChatRequest,
    current_user: str = Depends(get_current_user)
):
    try:
        completion = await llm_service.get_completion(
            prompt=request.prompt,
            max_tokens=request.max_tokens
        )
        if not isinstance(completion, str):
            logger.error(f"Unexpected completion type: {type(completion)}")
            raise HTTPException(
                status_code=500,
                detail="Unexpected response format from LLM service"
            )
        
        return ChatResponse(completion=completion)
    
    except Exception as e:
        logger.error(f"Error in completion endpoint: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing request: {str(e)}"
        )