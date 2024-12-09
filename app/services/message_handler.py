import json
import logging
from typing import Dict, Any, Callable

from app.solver.tlp_solver import tlp_solver
from app.utils.encryption import Encryption
from ..utils.websocket_handler import WebSocketHandler

logger = logging.getLogger(__name__)


class MessageHandler:
    def __init__(self, websocket_handler: WebSocketHandler):
        self.ws_handler = websocket_handler
        self.message_handlers: Dict[str, Callable] = {
            "pong": self._handle_pong,
            "tlpSolverRequest": self._handle_tlp_solver_request,
            # Add more message type handlers here
        }

    async def handle_message(self, data: dict):
        """Route messages to appropriate handlers based on type"""
        message = json.loads(data)
        message_type = message.get("type")
        if message_type in self.message_handlers:
            await self.message_handlers[message_type](message)
        else:
            logger.warning(f"Unknown message type: {message_type}")

    async def _handle_pong(self, message: dict):
        """Handle pong response from server"""
        logger.info("Received pong from server")

    async def _handle_tlp_solver_request(self, message: dict):
        """Handle TLP solver request"""
        data = message.get("data")
        t = data.get("t")
        baseg = data.get("baseg")
        product = data.get("product")
        key = data.get("assignment_key")
        ans = await tlp_solver(t=t, baseg=baseg, product=product)
        
        response = {
            "type": "tlpSolverResponse",
            "data": {"answer": int(ans), "assignment_key": key},
        }
        logger.info(f"Response to send: {response}")

        await self.ws_handler.send_message(json.dumps(response))
        # Implement logic to solve TLP here

    async def send_ping(self):
        """Send ping message to server"""
        message = json.dumps({"type": "ping", "data": "{}"})
        await self.ws_handler.send_message(message)
        logger.debug("Sent ping to server")
