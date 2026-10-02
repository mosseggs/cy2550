# Note, requires the Cryptodome Library. 
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_file(input_file_path: str, output_file_path: str, key: bytes, chunk_size: int = 64 * 1024) -> None:
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

    # Um actually the command can do that for you
    cipher = AES.new(key, AES.MODE_CBC);

    # 4. Open and process the files
    with open(input_file_path, 'rb') as infile, open(output_file_path, 'wb') as outfile:
        outfile.write(cipher.encrypt(pad(infile.read(), AES.block_size)))


def main() -> None:
    encrypt_file("myfile.txt","hide.txt", b'\xC3\xA9\xC3\xA9\xC3\xA9\xC3\xA9\xC3\xA9\xC3\xA9\xC3\xA9\xC3\xA9\xC3\xA9\xC3\xA9\xC3\xA9\xC3\xA9\xC3\xA9\xC3\xA9\xC3\xA9\xC3\xA9');


if __name__=="__main__":
    main()
