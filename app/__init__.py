"""
Core initialization file for the WebSocket client application.
Sets up logging, imports, and essential configuration.
"""

import logging
from typing import Dict, Any
from .config import settings
from .utils.encryption import Encryption
from .utils.websocket_handler import WebSocketHandler
from .services.message_handler import MessageHandler
from .main import SolverClientApp

# Set up basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

__version__ = "1.0.0"

# Application factory
def create_app() -> SolverClientApp:
    """
    Factory function to create and configure the client application.
    
    Args:
        client_id (str): Unique identifier for the client
        
    Returns:
        ClientApp: Configured client application instance
    """
    try:
        return SolverClientApp()
    except Exception as e:
        logger.error(f"Failed to create application: {str(e)}")
        raise

# Make commonly used classes and functions available at package level
__all__ = [
    'create_app',
    'settings',
    'logger',
    'ClientApp',
    'WebSocketHandler',
    'MessageHandler',
    'Encryption'
]