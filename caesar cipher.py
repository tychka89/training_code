print('Это программа "Шифр Цезаря"')

goal = input('Что нужно сделать? Введи: зашифровать или дешифровать  \n').lower()
while goal != 'зашифровать' and goal != 'дешифровать':
    goal = input('Что нужно сделать? Введи: зашифровать или дешифровать  \n').lower()

language = input('Какой язык используется? Введи: английский или русский   \n').lower()
while language != 'английский' and language != 'русский':
    language = input('Какой язык используется? Введи: английский или русский   \n').lower()

step = input('Какая будет длина шага?  Укажи число. \n')
while not step.isdigit():
    step = int(input('Какая будет длина шага?  Укажи число. \n'))

text = input('Введите текст  ')

def caesar_cipher(goal, language, step, text):

    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    rus_upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    for i in range(len(text)):
        if language == 'русский':
            letters = 32
            lower_alphabet = rus_lower_alphabet
            upper_alphabet = rus_upper_alphabet
        if language == 'английский':
            letters = 26
            lower_alphabet = eng_lower_alphabet
            upper_alphabet = eng_upper_alphabet

        if text[i].isalpha():

            if text[i] == text[i].lower():
                place = lower_alphabet.index(text[i])
            if text[i] == text[i].upper():
                place = upper_alphabet.index(text[i])

            if goal == 'дешифровать':
                index = (place - int(step)) % letters

            elif goal == 'зашифровать':
                index = (place + int(step)) % letters

            if text[i] == text[i].lower():
                print(lower_alphabet[index], end='')
            if text[i] == text[i].upper():
                print(upper_alphabet[index], end='')

        else:
            print(text[i], end='')

caesar_cipher(goal, language, step, text)