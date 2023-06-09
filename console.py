from cipher import Crypto
import os, click


crypt = Crypto()


@click.command()
@click.argument("crypt_or_decrypt")
@click.argument("path")
@click.argument("password")
@click.option(
    "--original_delete/--no-original_delete",
    "-od/-nod",
    help="Deleting the original file.",
    default=True,
)
@click.option(
    "--buffer-size",
    "-bs",
    help="The size of the decryption buffer.",
    default=524288,
)
def main(
    crypt_or_decrypt: str,
    path: str,
    password: str,
    original_delete: bool,
    buffer_size: int,
) -> None:
    """
    Encryptor and decryptor of files and directories\n
    Attention\n
    All information is provided for informational purposes only.
    The author is not responsible for any possible harm caused by the materials of this program.\n
    Instruction manual\n
    You need to enter three arguments:\n
    1. crypt_or_decrypt - Enter: "crypt" - if you want to encrypt "decrypt" - if you want to decrypt\n
    2. path - Enter the path to the directory or file.\n
    3. password - Enter the password.\n
    4. original_delete (optional) - Deleting the original file.\n
    5. buffer_size (optional) - The size of the decryption buffer.
    """
    print("[---Program Tech Crypto---]")
    if crypt_or_decrypt != "crypt" and crypt_or_decrypt != "decrypt":
        print("Wrong input! Enter crypt or decrypt!")
    if not os.path.exists(path):
        print(
            "The path to the directory or file is not correct. Enter an existing path!"
        )
    if crypt_or_decrypt == "crypt" and os.path.isdir(path):
        crypt.directory_crypt(
            path, password, buffer_size, original_delete=original_delete
        )
    if crypt_or_decrypt == "decrypt" and os.path.isdir(path):
        crypt.directory_decrypt(
            path, password, buffer_size, original_delete=original_delete
        )
    if crypt_or_decrypt == "crypt" and os.path.isfile(path):
        crypt.file_crypt(path, password, buffer_size, original_delete=original_delete)
    if crypt_or_decrypt == "decrypt" and os.path.isfile(path):
        crypt.file_decrypt(path, password, buffer_size, original_delete=original_delete)


if __name__ == "__main__":
    main()
