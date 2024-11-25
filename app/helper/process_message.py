import json
from app.model.alice_tlp_data import AliceTLPData


def process_message(message):
    """Process the message received from the BOB."""    
    print(f"Received message: {message}")    
    alice_message = AliceTLPData.from_dict(json.loads(message))
    return alice_message

