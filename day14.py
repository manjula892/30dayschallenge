import random
import string

print("🔐 Password Generator")

# Combine letters, digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)