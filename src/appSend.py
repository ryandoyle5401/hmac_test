import socket

from src.hmacHash import compute_hmac

# Shared secret key
secret_key = "mySecretKey"
# Secret message
message = "Hello, HMAC!"
# Generate the hash of secret_key and message with SHA-256
hmac_result = compute_hmac(message, secret_key)
# Create a client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the server to the localhost address and port 9999
client.connect(('127.0.0.1', 9999))
# Send a message to the server
client.send(hmac_result.encode())
print("Sent a message!")