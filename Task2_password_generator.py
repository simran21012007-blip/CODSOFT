import random
import string

# Function to validate y/n input
def get_choice(message):
    while True:
        choice = input(message).lower()

        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Please enter only y or n.")

# Function to generate password
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Generate a random password based on user preferences."""

    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type."

    password = "".join(random.choice(characters) for _ in range(length))
    return password


print("Welcome to the Password Generator!\n")

print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

# Validate password length
while True:
    try:
        length = int(input("Enter password length (8-32): "))

        if 8 <= length <= 32:
            break
        else:
            print("Password length must be between 8 and 32.")

    except ValueError:
        print("Invalid input! Please enter a number.")

# User choices
upper = get_choice("Include Uppercase letters? (y/n): ")
lower = get_choice("Include Lowercase letters? (y/n): ")
digits = get_choice("Include Numbers? (y/n): ")
symbols = get_choice("Include Symbols? (y/n): ")

# Generate password
password = generate_password(length, upper, lower, digits, symbols)

print("\n" + "=" * 40)

if password == "Please select at least one character type.":
    print(password)
else:
    print("Your Generated Password:")
    print(password)

print("=" * 40)