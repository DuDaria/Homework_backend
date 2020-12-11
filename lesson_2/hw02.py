
__author__ = 'Дю Д.Н.'

# Задача-1: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользоваться данным ресурсом можно только с 18 лет"

age = int(input("Привет, Сколько Вам лет: "))
if age > 18:
  print ("Доступ разрешен!")
else:
  print("Извините, пользоваться данным ресурсом можно только с 18 лет")
print("")

# Задача-2: Напишите программу, которая спрашивает "Четные или нечетные?",
# в зависимости от ответа, используя цикл с предусловием while или for in
# вывести в одну строку через пробел соотвествующие числа от 0 до 20
# Пример работы:
# $ "Четные или нечетные?"
# четные
# 0 2 4 6 8 10 12 14 16 18 20
# $ "Четные или нечетные?"
# нечетные
# 1 3 5 7 9 11 13 15 17 19
# $ "Четные или нечетные?"
# qwerty (или любая другая строка)
# Я не понимаю, что вы от меня хотите...

#1_Решение с while
even_or_odd = input ("Четные или нечетные? ")
a = 0
if even_or_odd == "четные":
  while a < 21:
    if a % 2 == 0:
      print(a, end = " ")
    a +=1
elif even_or_odd == "нечетные":
  while a < 20:
    if a % 2 == 1:
      print(a, end = " ")
    a +=1
else:
  print("Я не понимаю, что вы от меня хотите...")
print("\n")

#2_Решение с for in
even_or_odd = input ("Четные или нечетные? ")
if even_or_odd == "четные":
  for i in range(21):
    if i%2 == 0:
      print(i , end = " ")
elif even_or_odd == "нечетные":
  for i in range(21):
    if i%2 != 0:
        print(i , end = " ")
else:
  print("Я не понимаю, что вы от меня хотите...")
print("\n")

# Задача-3: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

# арифметика и цикл while
x = 58375
m = x%10
x = x//10
while x > 0:
    if x%10 > m:
      m = x%10
    x = x//10
print("max number = ", m)
print("")

#с применением цикла for
num = 58375
lst = list(str(num))
maximum = lst[0]
for number in lst:
  if  number > maximum:
    maximum = number
print("max number = ", maximum)
