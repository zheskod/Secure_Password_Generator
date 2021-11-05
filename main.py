from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

print('Добро пожаловать в Генератор случайных паролей!')
print('Для правильной генерации паролей нам нужны данные, введите их ниже!')

def generate_password(length, chars):
    return print(*sample(chars, length), sep='')


quantity = 0
while int(quantity) <= 0:
    quantity = int(input('Сколько паролей сгенерировать?: '))
    continue

len_password = 0
while int(len_password) <= 0:
    len_password = int(input('Введите длину одного пароля: '))
    continue

number_password = input('Будут ли пароль содержать цифры? (ДА/НЕТ): ')
if number_password == 'ДА':
    chars += digits

char_upper_password = input('Будет ли пароль содержать прописные буквы? (ДА/НЕТ): ')
if char_upper_password == 'ДА':
    chars += lowercase_letters

char_lower_password = input('Будет ли пароль содержать строчные буквы? (ДА/НЕТ): ')
if char_lower_password == 'ДА':
    chars += uppercase_letters

symbol_password = input('Будет ли пароль содержать символы? (ДА/НЕТ): ')
if symbol_password == 'ДА':
    chars += punctuation

ambiguous_char = input('Исключить не однозначные символы? (il1Lo0O) (ДА/НЕТ): ')

print('А вот и ваши пароли:')
for _ in range(quantity):
    generate_password(len_password, chars)
