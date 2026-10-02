# I hate this. Ewewewewwewewewewewewewe
# I asked justin in person if we'd ever have to do something like this and they said *NO*
# Gemini??? I think??? Whichever one is the shitty AI that keeps appearing on google searches. Gemini probably.
# I wrong “Write me a Python function that encrypts a file with AES.” into google. And took the 2nd part it gave bc the first part was just asking me to have a library installed. 

import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_file(input_file_path: str, output_file_path: str, key: bytes, chunk_size: int = 64 * 1024):
    """
    Encrypts a file using AES-256 (CBC mode) in chunks.
    
    :param input_file_path: Path to the file you want to encrypt.
    :param output_file_path: Path where the encrypted file should be saved.
    :param key: A cryptographically secure 32-byte key (for AES-256).
    :param chunk_size: Size of the chunks processed at a time (must be a multiple of 16).
    """
    # 1. Validate key length (32 bytes = 256 bits)
    if len(key) != 32:
        raise ValueError("Key must be exactly 32 bytes long for AES-256.")
        
    # 2. Generate a secure random 16-byte Initialization Vector (IV)
    iv = os.urandom(16)
    
    # 3. Initialize the AES cipher in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # 4. Open and process the files
    with open(input_file_path, 'rb') as infile, open(output_file_path, 'wb') as outfile:
        # Write the IV to the very beginning of the encrypted file
        outfile.write(iv)
        
        while True:
            chunk = infile.read(chunk_size)
            if len(chunk) == 0:
                break
                
            # If it's the final chunk, we must pad it to match the AES block size (16 bytes)
            if len(chunk) < chunk_size:
                chunk = pad(chunk, AES.block_size)
                outfile.write(cipher.encrypt(chunk))
                break
            else:
                outfile.write(cipher.encrypt(chunk))
