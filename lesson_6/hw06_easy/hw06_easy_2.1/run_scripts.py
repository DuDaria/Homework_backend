import os
import script_create_dir as cds
import script_del_dir as cdd

print("Текущая деректория:", os.getcwd())

cds.make_dir() 

print("Директории можно удалить.")
del_dir_input = input("Удаление директорий 'yes' или 'no': ")

if del_dir_input == 'yes':
    cdd.del_dir()
elif del_dir_input == 'no':
    print("Директории сохранены")
else:
    print("Не корректный ввод")

print('Программа завершена!')

