# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

# os.walk(top, topdown=True, onerror=None, followlinks=False)
# генерация имён файлов в дереве каталогов, сверху вниз 
# (если topdown равен True), либо снизу вверх (если False).
# Для каждого каталога функция walk возвращает кортеж 
# (путь к каталогу, список каталогов, список файлов).

import os

#1 Вариант через listdir
print("Текущая деректория:", os.getcwd())

def list_dir():
    lst_dir = os.listdir()
    
    for folder in lst_dir:
        if os.path.isdir(folder):
            print('Папка: {}'.format(folder))
list_dir()

print("")

#2 Вариант через os.walk
def list_dir_1():
    path = os.getcwd()
    # print(path)
    os_walk = os.walk(path)
    # print(tree)
    new_list = []

    for folder in os_walk:
        new_list.append(folder[1])
    # print(new_list)
    dir_list = new_list[0]
    for i in dir_list:
        print('Папка: {}'.format(i)) 

list_dir_1()
