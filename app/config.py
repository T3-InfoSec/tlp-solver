from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

class Settings(BaseSettings):    
    WEBSOCKET_URL: str = "ws://localhost:8000/ws/solver"
    PING_INTERVAL: int = 30  # seconds
    ENCRYPTION_KEY_PASSWORD: str
    class Config:
        env_file = ".env"


settings = Settings()
