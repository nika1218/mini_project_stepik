### CEZAR ###

# coздаем списки алфавитов
EN_alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
en_alf = 'abcdefghijklmnopqrstuvwxyz'
RU_alf = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ru_alf = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

# пользовательский блок
print('Введите sh, если хотите шифровать. Введите dsh, если хотите дешифровать')
type_shifr = input()
if type_shifr != 'sh' and type_shifr != 'dsh':  # проверка корректности ввода действия
    print('Ошибка ввода! Поробуйте снова!')
    exit(0)

print('Введите ru, если хотите использовать русский язык. Введите en, если хотите использовать английский язык')
ln = input()
if ln != 'ru' and ln != 'en':  # проверка корректности ввода языка
    print('Ошибка ввода! Поробуйте снова!')
    exit(0)

print('Введите шаг сдвига')
step = input()
if step.isdigit() != True:  # проверка корректности ввода шага
    print('Ошибка ввода! Поробуйте снова!')
    exit(0)
step = int(step) # однозначное опредление шага числом

print('Введите текст')
text = input()


# задаем мощность алфавита
if ln == 'en':
    n = len(en_alf)
elif ln == 'ru':
    n = len(ru_alf)


er = True # флаг ошибки (устанавливается False в случае если задан русский язык, а введен текст на английском языке и наоборот)
for i in range(len(text)):
    if ln == 'en' and ((text[i] in RU_alf)  or  (text[i] in ru_alf)):
        er = False
    elif ln == 'ru' and ((text[i] in EN_alf)  or  (text[i] in en_alf)):
        er = False
if er == False:
    print('Ошибка ввода! Поробуйте снова!')
    exit(0)

# основной блок
if type_shifr == 'sh':
    if ln == 'en': # блок  ШИФРОВАНИЯ на английском языке
        for i in range(len(text)):
            b = []
            if text[i] in EN_alf:
                a = EN_alf.find(text[i])
                k = (a + step) % n
                b = EN_alf[k]
            elif text[i] in en_alf:
                a = en_alf.find(text[i])
                k = (a + step) % n
                b = en_alf[k]
            elif text[i] in '0123456789 !?,.':
                b = text[i]
            print(*b, end='')

    elif ln == 'ru': # блок ШИФРОВАНИЯ на русском языке
        for i in range(len(text)):
            b = []
            if text[i] in RU_alf:
                a = RU_alf.find(text[i])
                k = (a + step) % n
                b = RU_alf[k]
            if text[i] in ru_alf:
                a = ru_alf.find(text[i])
                k = (a + step) % n
                b = ru_alf[k]
            if text[i] in '0123456789 !?,.':
                b = text[i]
            print(*b, end='')

elif type_shifr == 'dsh':
    if ln == 'en': # блок ДЕШИФРОВАНИЯ на английском языке
        for i in range(len(text)):
            b = []
            if text[i] in EN_alf:
                a = EN_alf.find(text[i])
                k = (a - step) % n
                b = EN_alf[k]
            elif text[i] in en_alf:
                a = en_alf.find(text[i])
                k = (a - step) % n
                b = en_alf[k]
            elif text[i] in '0123456789 !?,.':
                b = text[i]
            print(*b, end='')

    elif ln == 'ru': # блок ДЕШИФРОВАНИЯ на русском языке
        for i in range(len(text)):
            b = []
            if text[i] in RU_alf:
                a = RU_alf.find(text[i])
                k = (a - step) % n
                b = RU_alf[k]
            elif text[i] in ru_alf:
                a = ru_alf.find(text[i])
                k = (a - step) % n
                b = ru_alf[k]
            elif text[i] in '0123456789 !?,.':
                b = text[i]
            print(*b, end = '')


