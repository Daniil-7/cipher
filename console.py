from crypto1 import Crypto

if __name__ == "__main__":
    print("[---Program Tech Crypto---]")
    crypt_or_decrypt = str(
        input(
            "Введите:\ncrypt - если вы хотите зашифровать\ndecrypt - если хотите расшифровать\n>> "
        )
    )
    path_user = str(input("Введите путь к директории:\n>> "))
    password_user = str(input("Введите пароль:\n>> "))
    crypt = Crypto()
    if crypt_or_decrypt == "crypt":
        crypt.walk_crypt(path_user, password_user)
    if crypt_or_decrypt == "decrypt":
        crypt.walk_decrypt(path_user, password_user)
