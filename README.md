# encryption_decryption

Overview:
This is a simple encryption and decryption tool using the cryptography.fernet module in Python. It allows users to securely encrypt and decrypt messages using a symmetric key.

Features:
Generates a unique encryption key (if not already present).
Encrypts user-input messages.
Decrypts encrypted messages using the stored key.
Provides a user-friendly menu for interaction.

Prerequisites:
Python 3.x installed on your system.
cryptography module installed (pip install cryptography).

How It Works:
The script checks for an existing encryption key (secret.key).
If no key is found, a new one is generated and stored.
The user can choose to encrypt a message, decrypt an existing message, or exit.
