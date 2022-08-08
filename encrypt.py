from cryptography.fernet import Fernet
import os
import json


def generate_key(key_path: str = "keys.json", key_id: str = None):
    key = Fernet.generate_key()
    if os.path.exists(key_path):
        # if the json file already exists
        with open(key_path, "r") as key_file:
            content = key_file.read()
        print(content)
        compiled_content = json.loads(content)
        compiled_content[key_id] = key.decode()
    else:
        compiled_content = {key_id: key.decode()}

    with open(key_path, "w") as key_file:
        key_file.write(json.dumps(compiled_content, indent=4))

    return key


def load_keys_dict(key_path="keys.json") -> dict:
    with open(key_path, "r") as key_file:
        content = key_file.read()
    compiled_content = json.loads(content)
    return compiled_content


def encrypt_file(path: str, key):
    """ Given a key and a path of a file, encrypt the file"""

    f = Fernet(key)
    with open(path, "rb") as target_file:
        content = target_file.read()

    encrypted_content = f.encrypt(content)
    try:
        with open(path, "wb") as target_file:
            target_file.write(encrypted_content)
    except PermissionError:
        print(f"permission denied: {path}")


def decrypt_file(path: str, key):
    """ Given a key and a path of a file, decrypt the file"""

    if "desktop.ini" in path:
        return
    f = Fernet(key)
    with open(path, "r") as target_file:
        encrypted_content = target_file.read().encode()

    decrypted_content = f.decrypt(encrypted_content)
    with open(path, "wb") as target_file:
        target_file.write(decrypted_content)


def encrypt_folder(path: str = None, key_path: str = "keys.json"):
    """encrypt all files in a folder (including in sub-folders)"""
    if path is None:
        path = os.getcwd()  # if a path is not specified, encrypt all files in the current working directory.

    for path, directories, files in os.walk(path):
        for file in files:
            file_path = os.path.join(path, file)
            current_key = generate_key(key_id=file_path, key_path=key_path)
            encrypt_file(file_path, current_key)


def decrypt_folder(path: str = None):
    """decrypt all the files in the folder (including in subfolders)"""
    if path is None:
        path = os.getcwd()
    keys_dict = load_keys_dict()

    for path, directories, files in os.walk(path):
        for file in files:
            file_path = os.path.join(path, file)
            try:
                current_key = keys_dict[file_path]
                decrypt_file(file_path, current_key.encode())
            except KeyError:
                print(f"couldn't decrypt the file {file_path}")


def main():
    pass

if __name__ == '__main__':
    main()
