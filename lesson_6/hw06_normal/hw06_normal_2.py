# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь "меню" выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os

def print_menu():
    print("Меню: ")
    print("1. Перейти в папку")
    print("2. Просмотреть содержимое текущей папки")
    print("3. Удалить папку")
    print("4. Создать папку")

print_menu()   

def go_to_folder(input_name_folder):
    """
    go to specified folder
    """
    try:
        os.chdir('{}'.format(input_name_folder))
        print('Вы успешно перешли в папку \'{}\''. format(input_name_folder))
    except FileNotFoundError:
        print("Не удается найти указанную папку: \'{}\'".format(input_name_folder))
    except OSError:
        print("Синтаксическая ошибка в имени папки")

def contents_curr_folder():
    """
    displays the current content folder
    """
    for file in os.listdir():
        print('{}'.format(file))

def del_folder(input_name_folder):
    """
    del direct and checks for del
    """
    try:
        os.rmdir('{}'.format(input_name_folder))
        print('Папка \'{}\' удалена'. format(input_name_folder))
    except FileNotFoundError:
        print("Не удается найти указанную папку: \'{}\'".format(input_name_folder))
    except OSError:
        print("Синтаксическая ошибка, либо папка \'{}\' не пустая".format(input_name_folder))
        
def create_folder(input_name_folder):
    """
    creates folder and checks for created
    """
    try:
        os.mkdir('{}'.format(input_name_folder))
        print('Папка \'{}\' создана'. format(input_name_folder))
    except FileExistsError:
        print('Папка \'{}\' уже существует'.format(input_name_folder))
    except OSError:
        print("Синтаксическая ошибка в имени папки")   
    
try:
    while input("Выйти из меню 'y' если нет, то нажмите любую клавишу: ") != "y":
        n = int(input("Выберите пункт меню: "))
        
        if n == 1:
            input_name_folder = input("Введите название папки для перехода: ")
            go_to_folder(input_name_folder)    
        elif n == 2:
            print("Содержимое текущей папки: ")
            contents_curr_folder()
        elif n == 3:
            input_name_folder = input("Введите название папки для удаления: ")
            del_folder(input_name_folder)
        elif n == 4:
            input_name_folder = input("Введите название папки для создания: ")
            create_folder(input_name_folder)
        else:
            print("Извините такого пункта в меню нет.")

except ValueError:
    print ('Ошибка, не правильно введено значение!')

print("Программа завершена!")


