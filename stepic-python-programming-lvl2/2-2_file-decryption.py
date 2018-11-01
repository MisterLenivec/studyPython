# Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать,
# какой из паролей служит ключом для расшифровки файла с интересной информацией.

from simplecrypt import encrypt, decrypt, DecryptionException

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt", "rb") as ouf:
    for line in ouf:
        try:
            s = decrypt(line.strip(), encrypted).decode('utf8')
        except DecryptionException:
            print('DecryptionException')
        except:
            print('except')
        else:
            print(s)
