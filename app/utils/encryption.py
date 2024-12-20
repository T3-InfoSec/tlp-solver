from ..config import settings
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib

class Encryption:

    def __init__(self):
        password = settings.PLACEHOLDER_ENCRYPTION_KEY_PASSWORD.encode()
        self.key = hashlib.sha256(password).digest()

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_GCM)
        iv = cipher.iv
        ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
        # Combine IV and ciphertext, encode to base64
        return base64.b64encode(iv + ciphertext).decode()

    def decrypt(self, encrypted_text):
        raw = base64.b64decode(encrypted_text)
        iv = raw[:AES.block_size]
        ciphertext = raw[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_GCM, iv)
        return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()
