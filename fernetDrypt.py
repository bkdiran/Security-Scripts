from cryptography.fernet import Fernet

# Define your key and encrypted data
key = b'key_text'

encrypted_data = b'cipher_text'

# Initialize the Fernet cipher suite with the key
cipher_suite = Fernet(key)

# Decrypt the data
decrypted_data = cipher_suite.decrypt(encrypted_data)

# Convert the decrypted data from bytes to a string
decrypted_code = decrypted_data.decode('utf-8')

# Print the decrypted code
print("Decrypted code:")

print(decrypted_code)
