from asyncio import sleep
from app.helper.process_message import process_message
from app.solver.tlp_solver import tlp_solver


async def handle_bob(websocket):
    """Handles a client connection."""

    print(f"BOB connected")
    async for message in websocket:
        processed_message = process_message(message)
        tlp_result = await tlp_solver(
            processed_message.baseg, processed_message.t, processed_message.product
        )
        tlp_result = str(tlp_result)
        await websocket.send(tlp_result)
        print("Sent message to BOB")
