import random
import string

def generate_strong_password(length=12, use_upper=True, use_digits=True, use_special=True):
    characters = string.ascii_letters
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (
            any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            (not use_special or any(c in string.punctuation for c in password))
        ):
            return password

def get_user_preferences():
    length = int(input("Enter desired password length: "))
    use_upper = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_special = input("Include special characters? (yes/no): ").lower() == "yes"
    return length, use_upper, use_digits, use_special

print("Welcome to the Strong Password Generator!")

while True:
    try:
        length, use_upper, use_digits, use_special = get_user_preferences()
        
        password = generate_strong_password(length, use_upper, use_digits, use_special)
        print("Generated strong password:", password)
        
        generate_another = input("Do you want to generate another strong password? (yes/no): ")
        if generate_another.lower() != "yes":
            break
    except ValueError:
        print("Invalid input. Please enter valid values.")
