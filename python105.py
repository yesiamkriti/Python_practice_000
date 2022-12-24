import re

def check_password_strength(password):
  # Check if the password is at least 8 characters long
  if len(password) < 8:
    return False

  # Check if the password contains at least one lowercase letter, one uppercase letter, and one digit
  if not re.search(r'[a-z]', password):
    return False
  if not re.search(r'[A-Z]', password):
    return False
  if not re.search(r'\d', password):
    return False

  # Check if the password contains any special characters
  if not re.search(r'[^a-zA-Z\d]', password):
    return False

  # If all checks pass, return True
  return True