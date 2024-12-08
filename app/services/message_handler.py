import logging
from typing import Dict, Any, Callable
from ..utils.websocket_handler import WebSocketHandler

logger = logging.getLogger(__name__)

class MessageHandler:
    def __init__(self, websocket_handler: WebSocketHandler):
        self.ws_handler = websocket_handler
        self.message_handlers: Dict[str, Callable] = {
            "pong": self._handle_pong,
            # Add more message type handlers here
        }

    async def handle_message(self, message: dict):
        """Route messages to appropriate handlers based on type"""
        message_type = message.get("type")
        if message_type in self.message_handlers:
            await self.message_handlers[message_type](message)
        else:
            logger.warning(f"Unknown message type: {message_type}")

    async def _handle_pong(self, message: dict):
        """Handle pong response from server"""
        logger.info("Received pong from server")

    async def send_ping(self):
        """Send ping message to server"""
        await self.ws_handler.send_message({"type": "ping"})
        logger.debug("Sent ping to server")
