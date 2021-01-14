# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os

path = os.path.join('data', 'fruits.txt')

# Список больших букв русского алфавита:
alphabet = (list(map(chr, range(ord('А'), ord('Я')+1))))

with open(path, 'r', encoding='UTF-8') as w:
    
    list_fruits = []

    for i in w:
        if not i.isspace():
            string = i.replace('\n', "")
            list_fruits.append(string)
    
for item in list_fruits:
    dict_fruit = {}
    k = item[0][0]

    if k in alphabet:
        file_name = 'fruits_' + k + '.txt'
 
        path = os.path.join('data', file_name)

        def check(fruit):
            return True if fruit[0] == k else False

        result = filter(check, list_fruits)

        with open(path, 'w', encoding='UTF-8') as w:
            fruit_alphabet = list(result)
            for i in fruit_alphabet:
                w.write(i)
                w.write('\n')
            #print("Файл успешно создан!")
print("Программа завершена!")
