# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили

def convert(km=1):
    miles = int(km) * float(1.609)
    print(miles)

convert(20)

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    ndigits = 10**ndigits
    number = int(number * (ndigits + 0.2)) / ndigits
    print(number)
    pass

my_round(2.1234567, 5)
my_round(2.1999967, 5)
my_round(2.9999967, 5)
print()

# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# либо False (если несчастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    ticket_number = list(ticket_number)

    if len(ticket_number) == 6:
        ticket_num_1 = (ticket_number)[:3]
        ticket_num_2 = (ticket_number)[3:]

        def num(half_ticket):
            Sum_half_ticket = 0
            for i in half_ticket:
                i = int(i)
                Sum_half_ticket = Sum_half_ticket + i
            return Sum_half_ticket

        num(ticket_num_1)
        num(ticket_num_2)

        if num(ticket_num_1) == num(ticket_num_2):
            return True
        else:
            return False
    else:
        return False

print(lucky_ticket(123006))
print(lucky_ticket(12321)) 
print(lucky_ticket(436751))

print(lucky_ticket(436759))
print("")

# True
# False
# True
# False