import asyncio
from websockets.server import serve

from app.websocket.ws_client_handler import handle_bob



async def start_ws_server():
    """Starts the WebSocket server."""
    # Listens for incoming connections from client (Bob)
    host = "localhost"
    port = 8085
    print(f"Starting server on ws://{host}:{port}")

    async with serve(handle_bob, host, port):
        await asyncio.Future()
