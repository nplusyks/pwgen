#!/usr/bin/python3
import string, sys
from random import *
try:
  pwlenght = int(sys.argv[1])
  characters = string.ascii_letters + string.digits
  password =  "".join(choice(characters) for x in range(pwlenght))
  print(password)
except:
  print("Usage: ./pwgenerator.py <password lenght>")

