import jwt
import requests
import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


                                                    # Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

                                                    # Convert private key to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
).decode('utf-8')


                                                    # Convert public key to PEM format
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode('utf-8')


                                                    # Payload to be encrypted in JWT
payload = {
    'login': "admin",
    'password': "admin",
    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)
}


                                                    # Generate JWT with RSA encryption
encrypted_jwt = jwt.encode(
    payload,
    private_pem,
    algorithm='RS256'
)



                                                    # Convert JWT bytes to string
token = encrypted_jwt.decode('utf-8')


                                                # Update API URL
api_url = 'localhost:3000/login'


                                                # Update headers to include the JWT
headers = {'Authorization': 'Bearer ' + token}  # Note the space after 'Bearer'


                                                # Make API request with the JWT in the headers
response = requests.get(api_url, headers=headers)


if response.status_code == 200:
    print("API call successful!")
    print("Response:", response.json())
else:
    print("API call failed with status code:", response.status_code)



