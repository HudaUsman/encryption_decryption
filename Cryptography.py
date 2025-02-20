from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def generate_key():
    """Generate a new encryption key and save it."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Load the saved encryption key."""
    if not os.path.exists(KEY_FILE):
        print("No key found! Generating a new one...")
        return generate_key()
    
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_message(message, cipher):
    """Encrypt a message."""
    return cipher.encrypt(message.encode())

def decrypt_message(encrypted_message, cipher):
    """Decrypt a message."""
    return cipher.decrypt(encrypted_message).decode()

# Load or generate key
key = load_key()
cipher = Fernet(key)

# Menu for user interaction
while True:
    print("\nChoose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        message = input("Enter a message to encrypt: ")
        encrypted_msg = encrypt_message(message, cipher)
        print("Encrypted Message:", encrypted_msg.decode())  # Convert bytes to string for display

    elif choice == "2":
        encrypted_input = input("Enter the encrypted message: ")
        try:
            decrypted_msg = decrypt_message(encrypted_input.encode(), cipher)
            print("Decrypted Message:", decrypted_msg)
        except:
            print("Decryption failed! Make sure the correct key is used.")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
