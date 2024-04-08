import random
import string

def create_code():
  caracter = string.ascii_letters + string.digits
  number = random.sample(caracter, 8)
  code = "".join(number)
  return code