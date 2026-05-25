from fastapi import FastAPI
from app.shared.config import settings
from app.shared.gemini import gemini_client

app = FastAPI(
    title="Loki",
    description="A Multi-agent job application assistant",
    version="0.0.1"
)

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "google_api_key": bool(settings.google_api_key),
        "database_url": bool(settings.database_url),
        "gemini_api": gemini_client.test_connection()
    }