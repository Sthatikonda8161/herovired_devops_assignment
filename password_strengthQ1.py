def check_password_strenght(password):
  if len(password) < 8:
    return False
  uppercase = False
  lowercase = False
  for char in password:
    if char.isupper():
      uppercase = True
    elif char.islower():
      lowercase = True
  if not uppercase or not lowercase:
    return False
  digit = False
  for char in password:
    if char.isdigit():
      digit = True
  if not digit:
    return False
  special_character = False
  for char in password:
    if char.isalnum():
      special_character = True
  if not special_character:
    return False
  return True

def main():
  password = input("Enter the password to check the strength : ")
  if check_password_strenght(password):
    print("The password is strong")
  else:
    print("The password is not strong")
if __name__ == "__main__":
  main()


  
