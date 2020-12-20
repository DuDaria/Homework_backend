# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
fructs = ["яблоко", "банан", "киви", "арбуз"]
for index, fruit in enumerate (fructs, 1):
    print(f"{index}.",'{:>7}'.format(fruit))
print("")

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

lst_1 = [1, 2, 3, 4]
lst_2 = [3, 6, 7, 8, 9]
print(lst_1)
print(lst_2)

for i in lst_1.copy():
    if i in lst_2:
        lst_1.remove(i)
print(lst_1)
print(lst_2)
print("")

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
old_list = [4, 5, 6, 7]
new_list = []
for i in old_list:
    if i % 2 == 0:
        i /= 4
    elif i % 2 != 0:
        i *= 2
    new_list.append(i)

print(new_list)