"""
Advanced Caesar Cipher Tool
Author: Hardik Rajotiya
Description: Encrypt, decrypt, and brute-force Caesar Cipher messages.
"""

def caesar(text, shift, mode='encrypt'):
    """Encrypt or decrypt text using Caesar Cipher"""
    result = ""
    for char in text:
        if char.isupper():
            base = 65
            result += chr((ord(char) - base + shift) % 26 + base)
        elif char.islower():
            base = 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def encrypt(text, shift):
    return caesar(text, shift, 'encrypt')

def decrypt(text, shift):
    return caesar(text, -shift, 'decrypt')

def brute_force(text):
    """Show all shifts with the most likely first"""
    print("\nBrute Force (most likely first):")
    results = []
    
    # Try all shifts and score by common English letters
    for shift in range(1, 26):
        decrypted = decrypt(text, shift)
        # Simple scoring: more 'e' and 't' = more likely
        score = decrypted.lower().count('e') + decrypted.lower().count('t')
        results.append((score, shift, decrypted))
    
    # Show best matches first
    results.sort(reverse=True)
    for score, shift, text in results:
        print(f"Shift {shift:2d}: {text}")

def main():
    print("=== Caesar Cipher Tool ===")
    
    while True:
        choice = input("\n1. Encrypt\n2. Decrypt\n3. Brute Force\n4. Quit\n> ")
        
        if choice == "1":
            message = input("Message: ")
            shift = int(input("Shift: "))
            print(f"Encrypted: {encrypt(message, shift)}")
            
        elif choice == "2":
            message = input("Message: ")
            shift = int(input("Shift: "))
            print(f"Decrypted: {decrypt(message, shift)}")
            
        elif choice == "3":
            message = input("Message: ")
            brute_force(message)
            
        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()