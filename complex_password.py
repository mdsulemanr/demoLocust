import random
import string


def generate_complex_password(length=12):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    random.shuffle(all_characters)

    # Ensure the length is at least 12 characters
    if length < 12:
        raise ValueError("Password length must be at least 12 characters")

    # Generate password
    password = random.sample(uppercase_letters, 1) + \
               random.sample(lowercase_letters, 1) + \
               random.sample(digits, 1) + \
               random.sample(special_characters, 1) + \
               random.sample(all_characters, length - 4)

    # Shuffle the password characters
    random.shuffle(password)

    # Convert the list to a string
    password = ''.join(password)

    return password


# Example: Generate a complex password with a default length of 12 characters
password = generate_complex_password()
print("Generated Password:", password)
