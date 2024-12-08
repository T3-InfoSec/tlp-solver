import websockets
import asyncio
import logging
from ..config import settings
from .encryption import Encryption

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebSocketHandler:
    def __init__(self, client_id: str):
        self.client_id = client_id
        self.url = f"{settings.WEBSOCKET_URL}/{client_id}"
        self.encryption = Encryption()
        self.websocket = None
        self.is_connected = False

    async def connect(self):
        """Establish WebSocket connection"""
        try:
            self.websocket = await websockets.connect(self.url)
            self.is_connected = True
            logger.info(f"Connected to WebSocket server as client {self.client_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to connect: {str(e)}")
            return False

    async def disconnect(self):
        """Close WebSocket connection"""
        if self.websocket:
            await self.websocket.close()
            self.is_connected = False
            logger.info("Disconnected from WebSocket server")

    async def send_message(self, message: dict):
        """Send encrypted message"""
        if not self.is_connected:
            raise ConnectionError("Not connected to WebSocket server")
        
        encrypted_data = self.encryption.encrypt_message(message)
        await self.websocket.send(encrypted_data)
        logger.debug(f"Sent message: {message}")

    async def receive_message(self) -> dict:
        """Receive and decrypt message"""
        if not self.is_connected:
            raise ConnectionError("Not connected to WebSocket server")
        
        encrypted_data = await self.websocket.recv()
        message = self.encryption.decrypt_message(encrypted_data)
        logger.debug(f"Received message: {message}")
        return message