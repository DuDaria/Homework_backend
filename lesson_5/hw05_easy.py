# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

# rand_list для задания №1 и №3
rand_list = [random.randint(-10, 10) for i in range(10)]

#1 через map и lambda
new_rand_list_1 = list(map(lambda x : x**2, rand_list))
print(new_rand_list_1)

#2 через генератор списков
new_r_ls = [item**2 for item in rand_list]
print(new_r_ls)
print("")

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# 1 Вариант через for
fruits_lst1 = ['Апельсин', 'Ананс', 'Киви', 'Банан', 'Груша']
fruits_lst2 =  ['Апельсин', 'Банан', 'Груша', 'Авокадо', 'Мандарин', 'Гранат']
fruts = []

for i in fruits_lst1:
    if i in fruits_lst2:
        fruts.append(i) 
    else:
        False
print(fruts)

# 2 Вариант с помощью фильтра и функции
def fru_in_fru(fru_lst):
    """ Эта функция
    сравнивает оба списка
    """
    if(fru_lst in fruits_lst2):
        return True
    else:
        return False

print('Отфильтрованный список:')
new_list_fruits = list(filter(fru_in_fru, fruits_lst1))
print (new_list_fruits)

# 3 c помощью генератора списков
new_fruits = [item for item in fruits_lst1 if item in fruits_lst2]
print(new_fruits)
print("")

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

# 1 Вариант через for
new_rand_list_2 = []

for i in rand_list:
    if i % 3 == 0 and i > 0 and i % 4 != 0:
        new_rand_list_2.append(i)
    else:
        pass

if not new_rand_list_2:
    print('Список пуст')
else:
    print(new_rand_list_2)

# 2 через генератор списков
new_rand_lst = [i for i in rand_list if i % 3 == 0 and i > 0 and i % 4 != 0]

if not new_rand_lst:
    print('Список пуст')
else:
    print(new_rand_lst)
