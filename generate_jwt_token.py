import json
import jwt
from cryptography.fernet import Fernet

# Function to read JSON data from a file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to encrypt JSON data
def encrypt_json(data, cipher):
    json_data = json.dumps(data).encode('utf-8')
    encrypted_data = cipher.encrypt(json_data)
    return encrypted_data

# Secret key for encryption
secret_key = Fernet.generate_key()
cipher_suite = Fernet(secret_key)

# File paths for JSON files
file_paths = [
    r"senior-project-spring-2024\Senior Project Data\internship.json",
    r"senior-project-spring-2024\Senior Project Data\news.json",
    r"senior-project-spring-2024\Senior Project Data\staff.json"
]

# Dictionary to store JSON data
json_data = {}

# Read data from each JSON file
for file_path in file_paths:
    data = read_json_file(file_path)
    json_data.update(data)

# Encrypt the JSON data
encrypted_data = encrypt_json(json_data, cipher_suite)

# Encode the encrypted data into a JWT token
token = jwt.encode({"data": encrypted_data}, secret_key, algorithm='HS256')

print("JWT Token:", token)
