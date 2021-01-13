import os
from script_create_dir import make_dir
from script_del_dir import del_dir

print("Текущая деректория:", os.getcwd())
try:
    make_dir() 
except NameError:
    print('Директории уже существуют.')

print("Директории можно удалить.")
del_dir_input = input("Удаление директорий 'yes' или 'no': ")

if del_dir_input == 'yes':
    del_dir()
elif del_dir_input == 'no':
    print("Директории сохранены")
else:
    print("Не корректный ввод")

print('Программа завершена!')

