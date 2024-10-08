# Password Generator.
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

print("Welcome to my password generator.")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers?\n"))
nr_symbols = int(input("How many symbols?\n"))

# print(nr_letters)
# print(nr_symbols)
# print(nr_numbers)

# Generate the password in sequence.
# password = ""
#
# for letter in range(0, nr_letters):
#     password += random.choice(letters)
#
# for number in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# for symbol in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# print(f"Your password is: {password}")

# Generate a password that does not follow a sequence.

password_list = []

for letter in range(0, nr_letters):
    password_list.append(random.choice(letters))

for number in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
