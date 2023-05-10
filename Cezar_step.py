# coздаем спискок алфавита
en_alf = 'abcdefghijklmnopqrstuvwxyz'
n = len(en_alf)

# пользовательский блок
print('Введите текст')
text = input()
t = text.lower()

# основной блок
freq=[]  # список частоты встречаемости букв a+e+t в строке
for i in range(n): # дешифруем строку с шагом от 0 до 26
    b = []   # временная дешефрованая строка в виде списка
    for j in range(len(t)):
        step = i
        if t[j] in en_alf:
            a = en_alf.find(t[j])
            k = (a - step) % n
            b.append(en_alf[k])
        elif t[j] in '0123456789 !?,.':
            b.append(t[j])
        s=''.join(b)  # преобразуем временную дешеврофаный список в строку
    count_a = 0  # счетчик частоты встречаемости буквы а
    count_e = 0  # счетчик частоты встречаемости буквы e
    count_t = 0  # счетчик частоты встречаемости буквы t
    for j in range(len(s)):  # блок подсчета частоты встречаемости букв a, e, t  в дешеврофанной строке
        if s[j] == 'a':
            count_a += 1
        elif s[j] == 'e':
            count_e += 1
        elif s[j] == 't':
            count_t += 1
    count_all = count_a+count_e+count_t  # частота встречаемости букв a+e+t в строке
    freq.append(count_all)  # дополнояем ранее созданный список частоты встречаемости букв a+e+t в строке
    M=max(freq)  #  Находим максимальную частототу в списке freq
    freq.index(M)  #  Находим индекс максимальной частоты, это и есть шаг дешифрования
print('Шаг дешифрования:', freq.index(M))

