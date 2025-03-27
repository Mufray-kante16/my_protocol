import logging

# Set up logging
logging.basicConfig(filename="protocol.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Example usage in your functions
logging.info("Server started and listening for connections.")
logging.error("An error occurred during data transmission.")
# Session-based billing tracking
user_billing = {}

def track_billing(user, data_usage):
    cost_per_mb = 0.05
    session_cost = data_usage * cost_per_mb
    if user in user_billing:
        user_billing# Store billing information
user_billing = {}

def track_billing(user, data_usage):
    cost_per_mb = 0.05
    session_cost = data_usage * cost_per_mb
    if user in user_billing:
        user_billingimport threading

# Multi-threaded receiver
def handle_client(conn, addr, key):
    print(f"Connected by {addr}")
    encrypted_data = conn.recv(1024)
    decrypted_message = decrypt_data(encrypted_data, key)
    print(f"Encrypted Data: {encrypted_data}")
    print(f"Decrypted Message: {decrypted_message}")
    conn.close()

def multi_threaded_receive_data(host, port, key):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Server is ready and waiting for connections...")
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr, key))
            thread.start()

import socket
from cryptography.fernet import Fernet

# Generate and load encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

# Encrypt and decrypt functions
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()

# Billing functionality
def calculate_billing(data_usage):
    cost_per_mb = 0.05  # Example cost per MB
    total_cost = data_usage * cost_per_mb
    return total_cost

# Data transmission (sender)
def send_data(host, port, message, key):
    encrypted_message = encrypt_data(message, key)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(encrypted_message)
        print(f"Data sent successfully. Encrypted: {encrypted_message}")
        data_usage_mb = len(encrypted_message) / (1024 * 1024)  # Convert bytes to MB
        cost = calculate_billing(data_usage_mb)
        print(f"Data Usage: {data_usage_mb:.4f} MB | Cost: ${cost:.2f}")

# Data reception (receiver)
def receive_data(host, port, key):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Waiting for connection...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            encrypted_data = conn.recv(1024)
            decrypted_message = decrypt_data(encrypted_data, key)
            print(f"Encrypted Data: {encrypted_data}")
            print(f"Decrypted Message: {decrypted_message}")

# Main program
if __name__ == "__main__":
    # Generate or load the encryption key
    # Run this once to generate the key file
    encryption_key = generate_key()
    
    # Uncomment the line below to use an existing key
    # encryption_key = load_key()

    # Example: Uncomment to test sender or receiver
    # For receiving:
    # receive_data("127.0.0.1", 65432, encryption_key)

    # For sending:
    # send_data("127.0.0.1", 65432, "Hello, secure world!", encryption_key)
import socket

# Function to send data
def send_data(host, port, data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data.encode())
        print("Data sent successfully.")

# Function to receive data
def receive_data(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Waiting for connection...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            received_data = conn.recv(1024).decode()
            print(f"Data received: {received_data}")

# Example: Test data sending and receiving
# Use one terminal for receiving and another for sending
# Uncomment the appropriate lines for each test

# For receiving:
# receive_data("127.0.0.1", 65432)

# For sending:
# send_data("127.0.0.1", 65432, "Hello, this is a test!")
from cryptography.fernet import Fernet

# Generate and save an encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    return key

# Load an existing encryption key
def load_key():
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

# Encrypt data
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

# Decrypt data
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()

# Example usage
if __name__ == "__main__":
    # Generate a key and save it (run this once to generate the key file)
    encryption_key = generate_key()

    # Or load the key (use this after the key is generated)
    # encryption_key = load_key()

    # Test encrypting and decrypting
    sample_data = "This is a test message."
    encrypted = encrypt_data(sample_data, encryption_key)
    decrypted = decrypt_data(encrypted, encryption_key)

    print(f"Original Data: {sample_data}")
    print(f"Encrypted Data: {encrypted}")
    print(f"Decrypted Data: {decrypted}")
# Function to calculate billing cost
def calculate_billing(data_usage):
    # Define cost per megabyte (example: $0.05 per MB)
    cost_per_mb = 0.05
    total_cost = data_usage * cost_per_mb
    return total_cost

# Example: Test the billing function
data_used = 50  # Example data usage in MB
cost = calculate_billing(data_used)
print(f"Total cost for {data_used}MB: ${cost:.2f}")
import socket

# Initialize the protocol
def start_protocol():
    print("Protocol Initialized")

# Billing system logic
def bill_initiator(data_usage):
    cost_per_mb = 0.05  # Example cost per MB
    total_cost = data_usage * cost_per_mb
    return total_cost

# Add more functions here for security, routing, etc.
