import os
import sys
from script_create_dir import make_dir
from script_del_dir import del_dir

print('sys.argv = ', sys.argv)
print("Текущая деректория:", os.getcwd())

try: 
    n = int(input("Укажите кол-во директорий: "))
    if n == 0:
        print("Количество директорий не может равняться 0")
    elif n > 0:
        n += 1
        try:
            name_dir = str(input("Укажите название директорий: "))
            make_dir(name_dir, n)
        except NameError:
            print("NameError")
        except OSError:
            print("OSError")
    
except ValueError:
    print ('Ошибка, не правильно введено значение!')

print("Директории можно удалить.")
del_dir_input = input("Удаление директорий 'yes' или 'no':")

if del_dir_input == 'yes':
    del_dir(name_dir, n)
elif del_dir_input == 'no':
    print("Директории сохранены")
else:
    print("Не корректный ввод")

print("Программа завершена!")
