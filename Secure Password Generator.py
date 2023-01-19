import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exceptions = 'il1Lo0O'

chars = ''

password_quantity = int(input('Сколько паролей вам нужно сгенерировать?  '))
length = int(input('Какой длины должен быть пароль?  '))
password_digits = input('Включать ли в пароль цифры от 0 до 9? (да/нет)  ')
password_uppercase = input('Включать ли в пароль прописные буквы? (да/нет)  ')
password_lowercase = input('Включать ли в пароль строчные буквы? (да/нет)  ')
password_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? (да/нет)  ')
password_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? (да/нет)  ')

if password_digits == 'да':
    chars += digits
if password_uppercase == 'да':
    chars += uppercase_letters
if password_lowercase == 'да':
    chars += lowercase_letters
if password_punctuation == 'да':
    chars += punctuation
if password_exceptions == 'нет':
    chars += exceptions

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

for _ in range(password_quantity):
    print(generate_password(length, chars))
