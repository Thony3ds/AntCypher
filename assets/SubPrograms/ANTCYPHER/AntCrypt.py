import codecs
import base64
from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import pad

def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    cipher_text = cipher.encrypt(pad(plain_text, DES.block_size))
    return cipher_text

def aes_cipher(text, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(text.encode())
    return ciphertext

def rot13(text):
    return codecs.encode(text, 'rot_13')

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def vigenere_cipher(text, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in text]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext

def caesar_cipher(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key * len(text)))

def encrypt_file(filename, file_exit, method, key=None):
    with open(filename, 'r') as file:
        text = file.read()

    if method == 'rot13':
        encrypted_text = rot13(text)
    elif method == 'base64':
        encrypted_text = base64_encode(text)
    elif method == 'caesar':
        encrypted_text = caesar_cipher(text, shift=key)
    elif method == 'xor':
        encrypted_text = xor_cipher(text, key)
    elif method == 'vigenere':
        encrypted_text = vigenere_cipher(text, key)
    elif method == 'aes':
        encrypted_text = aes_cipher(text, key)
    else:
        print("Méthode non reconnue")
        return

    with open(file_exit, 'w') as file:
        file.write(encrypted_text)

    print(f"Le fichier {filename} a été crypté avec succès en utilisant la méthode {method}.")