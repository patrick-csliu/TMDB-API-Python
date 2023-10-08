# pip install argon2-cffi cryptography
import os
import getpass
from cryptography.fernet import Fernet
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Initialize the Argon2 password hasher
password_hasher = PasswordHasher()

# Get a password from the user
password = getpass.getpass("Enter your encryption password: ")

# Hash the password using Argon2
password_hash = password_hasher.hash(password)

# Generate a random Fernet key for encryption
fernet_key = Fernet.generate_key()
fernet_cipher = Fernet(fernet_key)

# Encrypt a file
def encrypt_file(input_file, output_file):
    with open(input_file, 'rb') as file:
        file_data = file.read()

    encrypted_data = fernet_cipher.encrypt(file_data)

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

# Decrypt a file
def decrypt_file(input_file, output_file):
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = fernet_cipher.decrypt(encrypted_data)

    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

# Input and output file paths
input_file_path = 'input.txt'
encrypted_file_path = 'encrypted_file.bin'
decrypted_file_path = 'decrypted_file.txt'

# Encrypt the file
encrypt_file(input_file_path, encrypted_file_path)
print("File encrypted successfully.")

# Decrypt the file
try:
    decrypt_file(encrypted_file_path, decrypted_file_path)
    print("File decrypted successfully.")
except Exception as e:
    print("Decryption failed:", str(e))

# Verify the password
try:
    password_hasher.verify(password_hash, password)
    print("Password is correct.")
except VerifyMismatchError:
    print("Password is incorrect.")