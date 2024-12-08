from cryptography.fernet import Fernet
import json
from ..config import settings

class Encryption:
    def __init__(self):
        self.fernet = Fernet(settings.ENCRYPTION_KEY)

    def encrypt_message(self, message: dict) -> bytes:
        """Encrypt a dictionary message to bytes"""
        json_data = json.dumps(message)
        return self.fernet.encrypt(json_data.encode())

    def decrypt_message(self, encrypted_data: bytes) -> dict:
        """Decrypt bytes to a dictionary message"""
        decrypted_data = self.fernet.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())
