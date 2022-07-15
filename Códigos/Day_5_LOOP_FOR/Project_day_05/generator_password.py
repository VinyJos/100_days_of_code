import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(' Welcome to the PyPassword Generator!')
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input('How many symbols would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))

password = ''
my_password = []

for ln in range(0, nr_letters):
    #my_password.append(random.choice(letters)) da pra fazer assim também
    my_password += random.choice(letters)
for ln in range(0, nr_numbers):
    my_password += random.choice(numbers)
for ln in range(0, nr_symbols):
    my_password += random.choice(symbols)
for ln in range(0, len(my_password)):
    password += random.choice(my_password)
print(f'Here is your password: {password}')

'''pode usar também o random.shuffle(password_list)
para embaralhar sem precisar usar o ultimo for'''