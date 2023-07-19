from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import argparse

def pad(data):
    # Pad the data to be a multiple of AES block size (16 bytes)
    return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

def encrypt_file(key, file_path, output_file_path):
    with open(file_path, 'rb') as file:
        data = file.read()

    data = pad(data)
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(output_file_path, 'wb') as file:
        file.write(iv)
        file.write(cipher.encrypt(data))

def decrypt_file(key, file_path, output_file_path):
    with open(file_path, 'rb') as file:
        iv = file.read(AES.block_size)
        data = file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(data)
    
    with open(output_file_path, 'wb') as file:
        file.write(decrypted_data.rstrip(b"\0"))


def main():
    parser = argparse.ArgumentParser(description='AES File Encryption/Decryption Tool')
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help='Choose action: encrypt or decrypt')
    parser.add_argument('input_file', type=str, help='Input file path')
    parser.add_argument('output_file', type=str, help='Output file path')
    parser.add_argument('key', type=str, help='Encryption/Decryption key (must be 16, 24, or 32 bytes long)')

    args = parser.parse_args()

    key = args.key.encode('utf-8')

    if len(key) not in [16, 24, 32]:
        print("Key must be 16, 24, or 32 bytes long. That was ")
        print(len(key))
        return

    if args.action == 'encrypt':
        encrypt_file(key, args.input_file, args.output_file)
        print("Encryption successful!")
    elif args.action == 'decrypt':
        decrypt_file(key, args.input_file, args.output_file)
        print("Decryption successful!")

if __name__ == '__main__':
    main()