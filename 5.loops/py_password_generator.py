import random

print("Welcome to the Password generator.")

nr_letters = int(input("How many letters would you like? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_', '{', '}', '[', ']']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ,'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Soft version

password = ""

for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password += random_char

for sym in range(1, nr_symbols + 1):
    random_sym = random.choice(symbols)
    password += random_sym

for num in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    password += random_num

#hard version
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for sym in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for num in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

hard_password = ""
for char in password_list:
    hard_password += char


print(f"Your generated easy password is: {password}")
print(f"Your generated hard password is {hard_password}")