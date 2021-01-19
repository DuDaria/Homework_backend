"""
    ПРИМЕЧАНИЕ: Для решения задачи необходимо познакомиться с модулями os, sys, argparse!
    СМ.: https://pythonworld.ru/moduli/modul-os.html,
    https://pythonworld.ru/moduli/modul-sys.html,
    https://habr.com/ru/company/ruvds/blog/440654/

    Задача похожа на задачу 2 из normal, однако, имеет особенности. Вы можете использовать решения из задачи 2.

    Задача:
    Напишите небольшую консольную утилиту, позволяющую работать с папками и файлами.
    Утилита должна работать с помощью параметров и флагов, передаваемых скрипту в командной строке.
    Примеры:
        python hw06_hard.py -touch ../dir1/test.txt -ls ../dir1/
        python hw06_hard.py -rm ../dir1/test.txt -ls ../dir1/
        python hw06_hard.py -mkdir ../dir1/newdir -ls ../dir1/
        python hw06_hard.py -ls ../dir1/
        python hw06_hard.py -touch ../dir1/test.txt

        и.т.д.

    Используйте модули argparse (для разбора аргументов), os, sys.

    Утилита должна принимать следующие флаги и выполнять следующие действия:
    "-ls <путь до папки>" - Посмотреть все файлы и подпапки в папке
    "-touch <путь до нового файла>" - Создать файл
    "-rm <путь до файла>" - Удалить файл
    "-mkdir <путь до папки>" - Создать папку

    Каждый из представленных параметров не обязательный, но если не указать никакой, то утилита должна вывести
    уведомление, которая предлагает посмотреть --help.
    Предусмотреть обработку исключений, например, если пытаются посмотреть все файлы не у папки, а у файла и.т.д.
"""

import os
import sys
import argparse


input_path_1 = sys.argv[2:]
input_path_2 = sys.argv[3:]

if input_path_1:
    list_path_1 = list(input_path_1[0].split("/"))
    folder_name = list_path_1[1]
    file_name = list_path_1[2]
elif input_path_1 and input_path_2:
    list_fold = list(input_path_2[1].split("/"))
    list_fold = list_fold[1]
    ls_name = input_path_2[0]


parser = argparse.ArgumentParser(description="Parser") #Создаем экземпляр класса ArgumentParser.
# Добавляем в него информацию об ожидаемых параметрах с помощью 
# метода add_argument (по одному вызову на каждый параметр).
parser.add_argument('-touch', type=str, help='- Создать файл')
parser.add_argument('-rm', type=str, help='- Удалить файл')
parser.add_argument('-ls', type=str, help='- Посмотреть все файлы и подпапки в папке')
parser.add_argument('-mkdir', type=str, help='- Создать папку')


args = parser.parse_args()
print('args =', args)
touch = args.touch
mkdir = args.mkdir
ls = args.ls
rm = args.rm


def create_file(input_name_file):
	file = open(input_name_file, "w")

def create_folder(input_name_folder):
    """
    создает папку и проверяет наличие созданных
    """
    try:
        os.mkdir('{}'.format(input_name_folder))
        print('Папка \'{}\' успешно создана'.format(input_name_folder))
    except FileExistsError:
        print('Папка \'{}\' уже существует'.format(input_name_folder))
    except OSError:
        print("Синтаксическая ошибка в имени папки")


def list_dir():
	"""
	Посмотр все файлов и подпапок в папках
	"""
	os.listdir()

	for dirpath, dirnames, filenames in os.walk("."):
    # перебрать каталоги
		for dirname in dirnames:
			print("Каталог:", os.path.join(dirpath, dirname))
    # перебрать файлы
		for filename in filenames:
			print("Файл:", os.path.join(dirpath, filename))	

	
def go_to_folder(input_name_folder):
    """
    перейти в указанную папку
    """
    try:
        os.chdir('{}'.format(input_name_folder))
        print('Вы успешно перешли в папку \'{}\''.format(input_name_folder))
    except FileNotFoundError:
        print("Не удается найти указанную папку: \'{}\'".format(input_name_folder))
    except OSError:
        print("Синтаксическая ошибка в имени папки")

	
# Создать файл		
if touch:
	# print("ВЫПОЛНИЛСЯ touch")
	if folder_name in os.listdir():
		go_to_folder(folder_name)

		if file_name in os.listdir():
			print('Файл \'{}\' уже существует'.format(file_name))
		else:
			create_file(file_name)
			print ("Файл \'{}\' успешно создан!".format(file_name))

	else:
		print('Папка \'{}\' не найдена'.format(folder_name))
		while input("Создать папку 'y', для отмены нажмите любую клавишу: ") == "y":
			create_folder(folder_name)
			
# Создать папку		
elif mkdir:
	# print("ВЫПОЛНИЛСЯ mkdir")
	go_to_folder(folder_name)

	if folder_name in os.listdir():
		create_folder(file_name)

	else:
		while input("Создать указанную папку 'y', для отмены нажмите любую клавишу: ") == "y":
			create_folder(folder_name)
			
# Удалить файл			
elif rm:
	# print("ВЫПОЛНИЛСЯ rm")
	go_to_folder(folder_name)

	if file_name in os.listdir():
		go_to_folder(folder_name)
		os.remove(file_name)
		print ("Файл \'{}\' успешно удален!".format(file_name))
	else:
		print('Файл \'{}\' не найден'.format(file_name))

# Посмотреть все файлы и подпапки в папке		
elif ls:
	# print("ВЫПОЛНИЛСЯ ls")
	if folder_name in os.listdir():
		go_to_folder(folder_name)
		list_dir()
	else:
		go_to_folder(folder_name)

else:
    print("Not installed value, see --help")

if touch and ls:
	print("ДВА АРГУМЕНТА")
