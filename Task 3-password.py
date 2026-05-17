import random
import string

print("=== Password Generator ===")

length = int(input("Enter password length: "))

use_letters = input("Include letters? (y/n): ").lower() == 'y'
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

password = []

if use_letters:
    password.append(random.choice(string.ascii_letters))
if use_digits:
    password.append(random.choice(string.digits))
if use_symbols:
    password.append(random.choice(string.punctuation))

all_chars = ""
if use_letters:
    all_chars += string.ascii_letters
if use_digits:
    all_chars += string.digits
if use_symbols:
    all_chars += string.punctuation

remaining_length = length - len(password)

for i in range(remaining_length):
    password.append(random.choice(all_chars))

# shuffle password
random.shuffle(password)

print("Generated Password:", "".join(password))
