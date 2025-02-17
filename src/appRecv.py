import socket

from src.hmacHash import compute_hmac

# Shared secret key
secret_key = "mySecretKey"
# Secret message
message = "Hello, HMAC!"
# Generate the hash of secret_key and message with SHA-256
hmac_result = compute_hmac(message, secret_key)
# Create a server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the server to the localhost address and port 9999
server.bind(('127.0.0.1', 9999))

# Listen for incoming connections
server.listen(1)
print("Server is listening for a connection...")

while True:
    # Accept a client connection and its address
    client, addr = server.accept()
    # Receive the message from the client
    msg = client.recv(1024).decode()
    print(msg)
    # Compare the generated hash to the hash that was sent
    if hmac_result == msg:
        print("Message has not been tampered with!")
    else:
        print("Message has been tampered with!")