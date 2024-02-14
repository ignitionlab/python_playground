import getpass
from uuid import getnode
from binascii import hexlify, unhexlify
import socket

def get_uid():
    original_text = getpass.getuser() + "-" + ":".join(f"{i:02X}" for i in getnode().to_bytes(6, 'big'))
    uid = hexlify(original_text.encode()).decode()
    return uid, original_text

# Call the function and print the result
result, original_text = get_uid()
print("Generated UID:", result)

# Convert the hexadecimal string back to the original text
decoded_text = unhexlify(result.encode()).decode()
print("Decoded Text:", decoded_text)

# Send the generated UID to the specified IP address and port
target_ip = "192.168.0.68"
target_port = 1337  # Change this to the desired port

# Create a socket and send the UID
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((target_ip, target_port))
        s.sendall(result.encode())
        print(f"UID sent to {target_ip}:{target_port}")
    except Exception as e:
        print(f"Error sending UID: {e}")