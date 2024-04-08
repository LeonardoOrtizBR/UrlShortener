from urllib.parse import urlparse

def verify_url(link):
  if not link:
    return False
  try:
    parsed_url = urlparse(link)
  except ValueError:
    return False
  if not parsed_url.scheme or parsed_url.scheme not in ["http", "https"]:
    return False
  if not parsed_url.hostname:
    return False
  for char in link:
    if char in ["<", ">", "(", ")", "{", "}", ";", "'"]:
      return False
  return True