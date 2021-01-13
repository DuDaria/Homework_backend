# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os

def cur_copy_file():
    path = os.getcwd()
    file_end = os.path.basename(__file__)
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
