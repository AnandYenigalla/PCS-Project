import utils.constants as constants
import utils.file

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def create_rsa_key_pair():
    # Generates a RSA key pair.
    key = RSA.generate(2048)

    private_key = key.export_key()
    public_key = key.publickey().export_key()

    return private_key, public_key


def encrypt_data(public_key, data):
    public_key_obj = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(public_key_obj)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data


def decrypt_data(private_key, encrypted_data):
    public_key_obj = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(public_key_obj)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data.decode("utf-8")


def create_node_rsa_key_pair():
    private_key_path = constants.dir_path + "private_key"
    public_key_path = constants.dir_path + "public_key"

    private_key, public_key = create_rsa_key_pair()

    utils.file.store_file_to_fs(private_key_path, private_key)
    utils.file.store_file_to_fs(public_key_path, public_key)

    return private_key, public_key
