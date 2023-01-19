import random

def is_valid(num):

    #Проверяет, что text является целым числом от 1 до 100

    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False

#генерируем целое число от 1 до 100
number = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')
counter = 0
while True:
    n = input('Попробуйте угадать число от 1 до 100 ... ')
    #Если введенное число меньше загаданного числа, выведите текст: 'Ваше число меньше загаданного, попробуйте еще разок';
    #Если введенное число больше загаданного числа, выведите текст: 'Ваше число больше загаданного, попробуйте еще разок';
    #Если введенное число равно загаданному числу, выведите текст: 'Вы угадали, поздравляем!'.
    if is_valid(n):
        counter += 1
        n = int(n)
        if n < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n < number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            print(f'Количество попыток {counter}')
            break
    else:
        print('А может быть все-таки введем число от 1 до 100?')


