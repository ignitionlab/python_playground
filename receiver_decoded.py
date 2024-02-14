import socket
from binascii import unhexlify

def start_listener():
    # Set the IP address and port to listen on
    host = "0.0.0.0"  # Listen on all available network interfaces
    port = 1337       # Make sure this matches the port used in the sender script

    # Create a socket to bind to the specified IP address and port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        print(f"Listening on {host}:{port}")

        # Allow up to 1 connection in the queue
        s.listen(1)

        # Wait for a connection
        conn, addr = s.accept()
        with conn:
            print(f"Connection from {addr}")

            # Receive data (in this case, the UID)
            data = conn.recv(1024)
            if data:
                # Decode the received hexadecimal UID to its original text
                decoded_text = unhexlify(data).decode()
                print(f"Received UID (Hex): {data.decode()}")
                print(f"Decoded Text: {decoded_text}")

if __name__ == "__main__":
    start_listener()
