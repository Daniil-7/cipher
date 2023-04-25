# Tech Crypto(Cipher)

## Description:
This library, written in the Python programming language, provides the ability to encrypt and decrypt files and directories using a password. It can be used to protect sensitive information such as personal data, financial information and other sensitive data.

The library provides functions for encrypting and decrypting files and directories using strong AES-256 encryption, which is one of the most secure encryption methods. A console command is also available, which allows you to use the library functionality from the command line.

This library can be used both for personal use and for commercial purposes to protect sensitive information. It provides a reliable and easy-to-use way to encrypt and decrypt files and directories using a password.

## Using the library in the code:
### The code provides a Python library that can encrypt and decrypt files and directories using the pyAesCrypt library. The library has four methods:

1. `file_crypt`: Encrypts a single file using pyAesCrypt. It takes in the file path, password, buffer size, logger, and original_delete as input arguments.

2. `file_decrypt`: Decrypts a single file using pyAesCrypt. It takes in the file path, password, buffer size, logger, and original_delete as input arguments.

3. `directory_crypt`: Recursively encrypts all files in a directory using pyAesCrypt. It takes in the directory path, password, buffer size, logger, title_logger, and original_delete as input arguments.

4. `directory_decrypt`: Recursively decrypts all files in a directory using pyAesCrypt. It takes in the directory path, password, buffer size, logger, title_logger, and original_delete as input arguments.

The `password` parameter is a string that is used as a key to encrypt and decrypt files. The `buffer_size` parameter is an integer that sets the size of the encryption and decryption buffer. The `logger` parameter is a boolean that determines whether the file paths are printed during the encryption and decryption process. The `original_delete` parameter is a boolean that determines whether the original file is deleted after encryption or decryption. The `title_logger` parameter is a boolean that determines whether a title is printed before starting the encryption or decryption process for the directory.

### Example of use:

1. `file_crypt()` method

The file_crypt() method is used to encrypt a single file. Example usage:
```python
from Crypto import Crypto

crypto = Crypto()

file = '/path/to/myfile.txt' # Путь к файлу, который нужно зашифровать
password = 'mypassword' # Пароль для шифрования

crypto.file_crypt(file, password)
```
In this example, we create a Crypto object, then specify the path to the file we want to encrypt and the password to encrypt it. We then call the file_crypt() method, which encrypts the file with the specified password. By default, the original file is deleted after encryption.


2. `file_decrypt()` method

The file_decrypt() method is used to decrypt a single file. Example usage:
```python
from Crypto import Crypto

crypto = Crypto()

file = '/path/to/myfile.txt.crp' # Путь к файлу, который нужно расшифровать
password = 'mypassword' # Пароль для расшифровки

crypto.file_decrypt(file, password)
```
In this example, we create a Crypto object, then specify the path to the file to decrypt and the password to decrypt it. Then we call the file_decrypt() method, which decrypts the file with the specified password. By default, the original file is deleted after decryption.


3. `directory_crypt()` method

The directory_crypt() method is used to encrypt all files in the specified directory and its subdirectories. Example usage:
```python
from Crypto import Crypto

crypto = Crypto()

directory = '/path/to/mydirectory' # Путь к директории, которую нужно зашифровать
password = 'mypassword' # Пароль для шифрования

crypto.directory_crypt(directory, password)

```
In this example, we create a Crypto object, then specify the path to the directory to be encrypted and the password for encryption. We then call the directory_crypt() method, which encrypts all files in the specified directory and its subdirectories with the specified password. By default, the original files are deleted after encryption.


4. `directory_decrypt()` method

The directory_decrypt() method is used to decrypt all files in the specified directory and its subdirectories. Example usage:
```python
from Crypto import Crypto

crypto = Crypto()

directory = '/path/to/mydirectory' 
password = 'mypassword' 

crypto.directory_decrypt(directory, password)
```
In this example, we create a Crypto object, then specify the path to the directory to be decrypted and the password for decryption. After that, we call the directory_decrypt() method, which decrypts all files in the specified directory and its subdirectories with the specified password. By default, the encrypted files are deleted after decryption.

