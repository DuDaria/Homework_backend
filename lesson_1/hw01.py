
__author__ = 'Дю Д.Н.'

# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

#Решение:
name = input("Введите Ваше имя: ")
age = int(input("Введите Ваш возраст: "))

if age < 18:
  result = 18 - age
  print(name, "на", result, "года/лет меньше 18")
if age > 18:
  result = age - 18
  print(name, "на", result, "года/лет больше 18")
  
print("")

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

#1_Решение:
a = int(input("Введите переменную \"а\": "))
b = int(input("Введите переменную \"b\": "))
c = a
a = b
b = c
print("a = ", a)
print("b = ", b)
print("")

#2_Решение
a1 = int(input("Введите переменную \"а\": "))
b1 = int(input("Введите переменную \"b\": "))
a1 = a1 + b1
b1 = a1 - b1
a1 = a1 - b1
print("a =", a1, ",", "b =", b1)
print("")

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

#Решение:
import math
#Дано квадратное ax2+bx+c=0 уравнение вычисляем его корни
print("Вычисление квадратного уравнения ax2+bx+c=0")
a2 = int(input("Введите \"а\": "))
b2 = int(input("Введите \"b\": "))
c2 = int(input("Введите \"с\": "))

#Дискриминант квадратного уравнения
D = (b2**2) - (4*a2*c2)

#Вычисление корней
if D > 0:
  x1 =(-b2 + math.sqrt(D))/(2 * a2)
  x2 = (-b2 - math.sqrt(D))/(2 * a2)
  print ("x1 =", x1,",", "x2 =", x2)
elif D == 0:
  x = -b2/(2 * a2)
  print("x = ", x)
else:
  print("Данное уравнение не имеет корней")
