# File Encryption

This is a simple file encryption program that uses the Advanced Encryption Standard and Cipher Block Chaining mode.
To use this program, first save the program to a directory. Then open a command line navigated to that directory. Then use the command

> python encryption.py encrypt [plaintext.txt] [ciphertext.txt] [key]

where the plaintext.txt is a text file you want to encrypt, ciphertext.txt is the output file for the encrypted message, and key is a 16/24/32 byte key used to encrypt the file.

To decrypt, run the command

> python encryption.py decrypt [ciphertext.txt] [output.txt] [key]

where ciphertext.txt is the same file from the previous encryption, output.txt will be the name of the output file, and key is the same key from before otherwise it will not work.
