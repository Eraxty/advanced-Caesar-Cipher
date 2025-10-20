# advanced_caesar_cipher.py
"""
Advanced Caesar Cipher Tool
Author: Hardik Rajotiya
Description: Encrypt, decrypt, and brute-force Caesar Cipher messages.
"""

def encrypt(text, shift):
    """Encrypt the text using Caesar Cipher"""
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    """Decrypt the text using Caesar Cipher"""
    return encrypt(text, -shift)

def brute_force(text):
    """Try all 25 possible shifts"""
    print("\n=== Brute Force Results ===")
    for shift in range(1, 26):
        decrypted = decrypt(text, shift)
        print(f"Shift {shift}: {decrypted}")

def main():
    print("=== Advanced Caesar Cipher Tool ===")
    while True:
        choice = input("\nChoose an option:\n1. Encrypt\n2. Decrypt\n3. Brute Force Decrypt\n4. Quit\n> ")
        if choice == "1":
            message = input("Enter message to encrypt: ")
            shift = input("Enter shift number (integer): ")
            if not shift.isdigit():
                print("Error: Shift must be an integer.")
                continue
            shift = int(shift)
            print(f"Encrypted message: {encrypt(message, shift)}")
        elif choice == "2":
            message = input("Enter message to decrypt: ")
            shift = input("Enter shift number used: ")
            if not shift.isdigit():
                print("Error: Shift must be an integer.")
                continue
            shift = int(shift)
            print(f"Decrypted message: {decrypt(message, shift)}")
        elif choice == "3":
            message = input("Enter message to brute-force decrypt: ")
            brute_force(message)
        elif choice == "4":
            print("Exiting Advanced Caesar Cipher Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

