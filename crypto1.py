import os
import pyAesCrypt


class Crypto:
    def __crypt(self, file, password, buffer_size, logger):
        pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, buffer_size)
        if logger:
            print(f"[Encrypt] '{str(file)}.crp'")
        os.remove(file)

    def __decrypt(self, file, password, buffer_size, logger):
        pyAesCrypt.decryptFile(
            str(file), str(os.path.splitext(file)[0]), password, buffer_size
        )
        if logger:
            print(f"[Decrypt] '{str(os.path.splitext(file)[0])}'")
        os.remove(file)

    def walk_crypt(
        self, directory, password, buffer_size=524288, logger=True, system_logger=True
    ):
        if logger and system_logger:
            print("[***Crypto***]")
        if logger:
            print(f"[Directory] '{directory}'")
        for name in os.listdir(directory):
            path = os.path.join(directory, name)
            if os.path.isfile(path):
                self.__crypt(path, password, buffer_size, logger)
            else:
                self.walk_crypt(path, password, buffer_size, logger, False)

    def walk_decrypt(
        self, directory, password, buffer_size=524288, logger=True, system_logger=True
    ):
        if logger and system_logger:
            print("[***Derypto***]")
        if logger:
            print(f"[Directory] '{directory}'")
        for name in os.listdir(directory):
            path = os.path.join(directory, name)
            if os.path.isfile(path):
                try:
                    self.__decrypt(path, password, buffer_size, logger)
                except Exception:
                    pass
            else:
                self.walk_decrypt(path, password, buffer_size, logger, False)
