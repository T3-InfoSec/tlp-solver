from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENCRYPTION_KEY_PASSWORD: str = "vh9qFH0T9hzlhF++Z8aQjuMi++JCS2cPXZRnlL3/Jk4="
    WEBSOCKET_URL: str = "ws://localhost:8000/ws/solver"
    PING_INTERVAL: int = 30  # seconds


settings = Settings()
