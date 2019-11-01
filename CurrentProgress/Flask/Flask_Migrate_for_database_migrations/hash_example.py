from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'supersecretpassword' #Haslo usera
hashed_password = bcrypt.generate_password_hash(password=password)

print(hashed_password) #Hash hasla
# Sprawdzenie

check = bcrypt.check_password_hash(hashed_password, 'supersecretpassword')
print(check)

#WERKZEUG example
from werkzeug.security import generate_password_hash, check_password_hash

hashed_pass = generate_password_hash('qwerty')
print(hashed_pass)

check = check_password_hash(hashed_pass, 'qwerty')
print(check)


