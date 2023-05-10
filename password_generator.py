### password_generator ###

# программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля,
# а также на то, какие символы требуется в него включить, а какие исключить.

from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars =[]
#chars = digits + lowercase_letters + uppercase_letters + punctuation

print('Сколько паролей требуется создать?')
count_password = int(input())

print('Ведите длину пароля')
Len_password = int(input())

print('Включать ли в пароль цифры?')
digit_password = input()

print('Включать ли в пароль прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
Up_password = input()

print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
Lo_password = input()

print('Включать ли символы !#$%&*+-=?@^_?')
S_password = input()

print('Исключать ли неоднозначные символы il1Lo0O?')
NS_password = input()

if digit_password.lower() == 'да' or digit_password.lower() == 'yes' or digit_password.lower() == 'lf':
    chars.append(digits)
if Up_password.lower() == 'да' or Up_password.lower() == 'yes' or Up_password.lower() == 'lf':
    chars.append(uppercase_letters)
if Lo_password.lower() == 'да' or Lo_password.lower() == 'yes' or Lo_password.lower() == 'lf':
    chars.append(lowercase_letters)
if S_password.lower() == 'да' or S_password.lower() == 'yes' or S_password.lower() == 'lf':
    chars.append(punctuation)

chars = ''.join(chars)
chars = list(chars)

if  NS_password.lower() == 'да' or NS_password.lower() == 'yes' or NS_password.lower() == 'lf': # Исключаем двойственные символы
    chars.remove('i')
    chars.remove('L')
    chars.remove('l')
    chars.remove('o')
    chars.remove('O')
    chars.remove('0')
    chars.remove('1')

for i in range(count_password):
    password = []
    for j in range(Len_password):
        a = choice(chars)
        password.append(a)
        PS = ''.join(password)
    print(PS)



