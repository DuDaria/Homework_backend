# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os

def cur_copy_file():
    path = os.getcwd()
    path_file = os.path.join(path, __file__)
    
    path_file = str(path_file)
    raw_str = r'{}'.format(path_file)

    list_file = raw_str.split('\\')
    file_end = list_file[-1]
    print(file_end)
    
    file_copy = 'copy_' + file_end
    print(file_copy)

    file1 = open(file_end,'r')
    file2 = open(file_copy,'w')

    file2.write(file1.read())

    file1.close()
    file2.close()

    print('Копия файла успешно создана!')

cur_copy_file()
