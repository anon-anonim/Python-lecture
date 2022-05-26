from simplecrypt import decrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

password_lst = []

file = open("passwords.txt", "r")
lines = file.readlines()
for line in lines:
    password_lst.append(line.strip())
file.close()

for password in password_lst:
    try:
        text = decrypt(password, encrypted)
    except:
        print(password, 'не верный')
    else:
        print(str(text).strip('b'))
        break
