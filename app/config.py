from cryptography.fernet import Fernet
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENCRYPTION_KEY: str = "5XKbXMqRAuGiN5nt2ZRKmRlYN1XpdpB_FROVDXG1QK8="
    WEBSOCKET_URL: str = "ws://localhost:8000/ws/solver"
    PING_INTERVAL: int = 30  # seconds

settings = Settings()