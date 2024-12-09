import asyncio
import logging

from app.utils.fingerprint import generate_fingerprint
from .utils.websocket_handler import WebSocketHandler
from .services.message_handler import MessageHandler
from .config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SolverClientApp:
    def __init__(self):
        client_id = generate_fingerprint()
        self.ws_handler = WebSocketHandler(client_id)
        self.message_handler = MessageHandler(self.ws_handler)
        self.running = False

    async def start(self):
        """Start the client application"""
        if not await self.ws_handler.connect():
            return

        self.running = True
        ping_task = asyncio.create_task(self._ping_loop())
        
        try:
            while self.running:
                message = await self.ws_handler.receive_message()                          
                await self.message_handler.handle_message(message)
        except Exception as e:
            logger.error(f"Error in main loop: {str(e)}")
        finally:
            ping_task.cancel()
            await self.ws_handler.disconnect()

    async def stop(self):
        """Stop the client application"""
        self.running = False
        await self.ws_handler.disconnect()

    async def _ping_loop(self):
        """Periodically send ping messages to keep connection alive"""
        while self.running:
            try:
                await self.message_handler.send_ping()
                await asyncio.sleep(settings.PING_INTERVAL)
            except Exception as e:
                logger.error(f"Error in ping loop: {str(e)}")
                break