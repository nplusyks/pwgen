#!/usr/bin/python3
import string, sys
from random import *
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

try:
  pwlenght = int(sys.argv[1])
  characters = string.ascii_letters + string.digits
  password =  "".join(choice(characters) for x in range(pwlenght))
  encryptedpw = fernet.encrypt(password.encode())
  print("original string:", password)
  print("\nencrypted string:", encryptedpw)
  
except:
  print("Usage: pwgenerator <password lenght>")


