# Advanced Caesar Cipher Tool 🔐

A Python implementation of the classic Caesar cipher with encryption, decryption, and brute force capabilities. Perfect for learning cryptography basics!

## Features

- ✅ **Encrypt and decrypt text** with custom shift values
- ✅ **Support for uppercase, lowercase, and special characters**
- ✅ **Brute force attack capability** to crack encrypted messages
- ✅ **Command-line interface** for easy use
- ✅ **Comprehensive unit tests** for reliability
- ✅ **Easy-to-use Python API** for integration
- ✅ **Educational examples** and documentation

## Installation

```bash
git clone https://github.com/yourusername/caesar-cipher-tool.git
cd caesar-cipher-tool
```
## Quick Start

```bash
python advanced_caesar_cipher.py
```
## 📘 Usage Examples

### Interactive Mode
When you run the script, you'll see an interactive menu:

```text
=== Advanced Caesar Cipher Tool ===

Choose an option:
1. Encrypt
2. Decrypt
3. Brute Force Decrypt
4. Quit
>
```

### Example 1 — Encryption
```text
Choose an option: 1
Enter message to encrypt: Hello World
Enter shift number (integer): 3
Encrypted message: Khoor Zruog
```

### Example 2 — Decryption
```
Choose an option: 2
Enter message to decrypt: Khoor Zruog
Enter shift number used: 3
Decrypted message: Hello World
```

### Example 3 — Brute Force Attack
```
Choose an option: 3
Enter message to brute-force decrypt: Khoor Zruog
=== Brute Force Results ===
Shift 1: Jgnnq Yqtnf
Shift 2: Ifmmp Xpsme
Shift 3: Hello World
Shift 4: Gdkkn Vnqkc
...
Shift 25: Lipps Asvph
```