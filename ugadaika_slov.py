### UGADAIKA SLOV ###

from random import *

word_list = ['гармонь', 'игра', 'баллерина', 'вилка', 'шар', 'телефон', 'стол', 'ель', 'тряпка', 'фото', 'пазл', 'мракобесие', 'крем', 'небо',
             'кружка', 'ручка', 'самолёт', 'орхидея', 'папка', 'провод', 'картина', 'календарь', 'ножницы', 'шкаф']
def get_word(): # функция выбора слова
    word = choice(word_list)
    word = word.upper()
    return(word)

def display_hangman(tries):
    stages = [ '''
             The END. Вы проиграли...
            --------
            |       |
            |       0
            |     \ | /
            |       |
            |      //
            - 
               ''',
               '''
                   голова, тело, руки, одна нога
                   --------
                   |      |
                   |      0
                   |     \|/
                   |      |
                   |     /
                   -
               ''',
               ''' голова, тело, руки
                                  --------
                                  |      |
                                  |      0
                                  |     \|/
                                  |      |
                                  |     
                                  -
               ''',
               '''
               голова, тело, рука
                   --------
                   |      |
                   |      0
                   |     \|
                   |      |
                   |     
                   -
               ''',
               '''
               голова и тело
                   --------
                   |      |
                   |      0
                   |      |
                   |      |
                   |     
                   -
               ''',
               '''
               голова
                   --------
                   |      |
                   |      0
                   |      
                   |      
                   |     
                   -
               ''',
               '''
               Старт!
                   --------
                   |      |
                   |      
                   |     
                   |      
                   |     
                   -
               ''']
    return stages[tries]

#def play():   # функция процесса игры
print('Давайте играть в угадайку слов!')
while True:
    tries = 6  # присваиваем начальное значение виселицы
    word = get_word()
    w = len(word) * '_'  # создаем строку загаданного слова
    w = list(w)  # переводим строку загаданного слова в список
    print(''.join(w))  # вывод длины загаданного слова
    print(display_hangman(tries)) # Вывод начальной виселицы

    while tries > 0:
        print("Введите букву или слово")
        litera = input().upper()
        if litera in word and len(litera) == 1: # провверка наличия введенной БУКВЫ в слове
            for i in range(len(word)):
                if word[i] == litera:
                    w[i] = litera
                    print(''.join(w))
                    print(display_hangman(tries))
        elif litera == word:  # проверка введенного СЛОВА
            print("Ура! Вы победили!")
            break
        else:  # действия в случае если ни буква, ни слово не угаданы
            tries -= 1
            print(''.join(w))
            print("Упс! Ошибочка..")
            print(display_hangman(tries))
    print("Если хотите играть снова введите +")
    new_game = input()
    if new_game == "+":
        continue
    else:
        print("Приходите поиграть еще!")
        break



