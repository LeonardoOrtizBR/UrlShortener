import re

def verify_short(text):
  special_characters = re.compile(r"[^a-zA-Z0-9]")
  return bool(special_characters.search(text))