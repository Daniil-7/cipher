import os
import pyAesCrypt


class Crypto:
    def file_crypt(self, file: str, password: str, buffer_size: int = 524288, logger: bool = True):
        """
        Encrypts a single file using pyAesCrypt.

        Args:
            file (str): The path to the file to encrypt.
            password (str): The password to use for encryption.
            buffer_size (int, optional): The size of the encryption buffer.
            logger (bool, optional): If True, print the path of the encrypted file.

        Returns:
            None
        """
        pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, buffer_size)
        if logger:
            print(f"[Encrypt] '{str(file)}.crp'")
        os.remove(file)

    def file_decrypt(self, file: str, password: str, buffer_size: int = 524288, logger: bool = True):
         """
        Decrypts a single file using pyAesCrypt.

        Args:
            file (str): The path to the file to decrypt.
            password (str): The password to use for decryption.
            buffer_size (int, optional): The size of the decryption buffer.
            logger (bool, optional): If True, print the path of the decrypted file.

        Returns:
            None
        """
        pyAesCrypt.decryptFile(
            str(file), str(os.path.splitext(file)[0]), password, buffer_size
        )
        if logger:
            print(f"[Decrypt] '{str(os.path.splitext(file)[0])}'")
        os.remove(file)

    def directory_crypt(
        self, directory: str, password: str, buffer_size: int = 524288, logger: bool = True, title_logger: bool = True
    ):
        """
        Recursively encrypts all files in a directory using pyAesCrypt.

        Args:
            directory (str): The path to the directory to encrypt.
            password (str): The password to use for encryption.
            buffer_size (int, optional): The size of the encryption buffer.
            logger (bool, optional): If True, print the path of each file as it is encrypted.
            title_logger (bool, optional): If True, print a title before starting the encryption process.

        Returns:
            None
        """
        if logger and title_logger:
            print("[***Crypto***]")
        if logger:
            print(f"[Directory] '{directory}'")
        for name in os.listdir(directory):
            path = os.path.join(directory, name)
            if os.path.isfile(path):
                self.file_crypt(path, password, buffer_size, logger)
            else:
                self.directory_crypt(path, password, buffer_size, logger, False)

    def directory_decrypt(
        self, directory: str, password: str, buffer_size: int = 524288, logger: bool = True, title_logger: bool = True
    ):
        """
        Recursively decrypts all files in a directory using pyAesCrypt.

        Args:
            directory (str): The path to the directory to decrypt.
            password (str): The password to use for decryption.
            buffer_size (int, optional): The size of the decryption buffer.
            logger (bool, optional): If True, print the path of each file as it is decrypted.
            title_logger (bool, optional): If True, print a title before starting the decryption process.

        Returns:
            None
        """
        if logger and title_logger:
            print("[***Derypto***]")
        if logger:
            print(f"[Directory] '{directory}'")
        for name in os.listdir(directory):
            path = os.path.join(directory, name)
            if os.path.isfile(path):
                try:
                    self.file_decrypt(path, password, buffer_size, logger)
                except Exception:
                    pass
            else:
                self.directory_decrypt(path, password, buffer_size, logger, False)
