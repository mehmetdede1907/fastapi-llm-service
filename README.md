# FastAPI LLM Service

A production-ready FastAPI service for LLM integration with support for monitoring and error tracking.

## Features

- FastAPI REST API
- Anthropic Claude Integration
- Structured Logging
- Authentication & Authorization
- Request Validation
- Error Handling
- Configuration Management

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fastapi-llm-service.git
cd fastapi-llm-service
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file:
```env
ENVIRONMENT=development
ANTHROPIC_API_KEY=your_api_key
SECRET_KEY=your_secret_key_for_jwt
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Documentation

Once running, visit:
- http://localhost:8000/docs for Swagger UI
- http://localhost:8000/redoc for ReDoc

## Authentication

The API uses JWT tokens for authentication. To get a token:

```bash
curl -X POST "http://localhost:8000/auth/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=demo&password=demo"
```

## License

MIT