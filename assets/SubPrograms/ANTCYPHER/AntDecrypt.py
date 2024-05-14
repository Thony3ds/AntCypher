from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import unpad
import base64, codecs

def des_decrypt(cipher_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plain_text = unpad(cipher.decrypt(cipher_text), DES.block_size)
    return plain_text

def decrypt_aes(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()

def decrypt_rot13(ciphertext):
    return codecs.decode(ciphertext, 'rot_13')

def decrypt_base64(ciphertext):
    return base64.b64decode(ciphertext).decode()

def decrypt_vigenere(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext

def decrypt_caesar(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            stay_in_alphabet = ord(char) - shift
            if char.isupper():
                if stay_in_alphabet > ord('Z'):
                    stay_in_alphabet -= 26
                elif stay_in_alphabet < ord('A'):
                    stay_in_alphabet += 26
            elif char.islower():
                if stay_in_alphabet > ord('z'):
                    stay_in_alphabet -= 26
                elif stay_in_alphabet < ord('a'):
                    stay_in_alphabet += 26
            plaintext += chr(stay_in_alphabet)
        else:
            plaintext += char
    return plaintext

def decrypt_xor(text, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key * len(text)))

def decrypt_file(filename, file_exit, method, key=None):
    with open(filename, 'r') as file:
        text = file.read()

    if method == 'rot13':
        encrypted_text = decrypt_rot13(text)
    elif method == 'base64':
        encrypted_text = decrypt_base64(text)
    elif method == 'caesar':
        encrypted_text = decrypt_caesar(text, shift=key)
    elif method == 'xor':
        encrypted_text = decrypt_xor(text, key)
    elif method == 'vigenere':
        encrypted_text = decrypt_vigenere(text, key)
    elif method == 'aes':
        encrypted_text = decrypt_aes(text, key)
    else:
        print("Méthode non reconnue")
        return

    with open(file_exit, 'w') as file:
        file.write(encrypted_text)

    print(f"Le fichier {filename} a été crypté avec succès en utilisant la méthode {method}.")