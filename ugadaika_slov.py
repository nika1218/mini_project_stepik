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
while True: # внешний цикл, что бы игра повторялась (при желани)
    tries = 6  # присваиваем начальное значение виселицы
    word = get_word()
    w_str = len(word) * '_'  # создаем строку загаданного слова
    w_spis = list(w_str)  # переводим строку загаданного слова в список
    print(''.join(w_spis))  # вывод длины загаданного слова
    print(display_hangman(tries)) # Вывод начальной виселицы
    litters = []

    while tries > 0:
        print("Введите букву или слово")
        littera = input().upper()
        litters.append(littera)
        flag = True
        if littera in word and len(littera) == 1: # провверка наличия введенной БУКВЫ в слове
            for i in range(len(word)):
                if word[i] == littera:
                    w_spis[i] = littera
                    a = ''.join(w_spis)
                    if a == word: # проверка на случай того, что введеная буква помогла угдать все слово
                        flag = False
                        break
                    print(a)
                    print(display_hangman(tries))
                    print("Вы вводили следующие буквы и слова:")
                    print(', '.join(litters))
            if flag == False:
                print("Ура! Вы победили!")
                print(a)
                break
        elif littera == word or flag == False:  # проверка введенного СЛОВА
            print("Ура! Вы победили!")
            print(a)
            break
        else:  # действия в случае если ни буква, ни слово не угаданы
            tries -= 1
            print(''.join(w_spis))
            print("Упс! Ошибочка..")
            print(display_hangman(tries))
            print("Вы вводили следующие буквы и слова:")
            print(', '.join(litters))
    print("Если хотите играть снова введите +")
    new_game = input()
    if new_game == "+":
        continue
    else:
        print("Приходите поиграть еще!")
        break



