import os
import pyAesCrypt


class Crypto:
    def file_crypt(self, file, password, buffer_size=524288, logger=True):
        pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, buffer_size)
        if logger:
            print(f"[Encrypt] '{str(file)}.crp'")
        os.remove(file)

    def file_decrypt(self, file, password, buffer_size=524288, logger=True):
        pyAesCrypt.decryptFile(
            str(file), str(os.path.splitext(file)[0]), password, buffer_size
        )
        if logger:
            print(f"[Decrypt] '{str(os.path.splitext(file)[0])}'")
        os.remove(file)

    def directory_crypt(
        self, directory, password, buffer_size=524288, logger=True, title_logger=True
    ):
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
        self, directory, password, buffer_size=524288, logger=True, title_logger=True
    ):
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
