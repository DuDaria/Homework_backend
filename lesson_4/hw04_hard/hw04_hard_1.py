# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

print("Сложение и вычитание дробей")
expression = input("Введите всё выражение целиком в виде строки: ")

# expression = '5/6 + 4/7'
# expression ='10 - 1/2'
# expression ='1/2 + 10'
# expression ='10 + 15'
# expression ='1 1/2 + 1 1/2'
# expression ='1 1/2 + 1'

oper = ['+', '-']

minus = " - "
plus = " + "
integer = "123456789-1-2-3-4-5-6-7-8-9"

lst_1 = []
lst_2 = []

def nam_fact(a):
    """десятичное
    """
    b = list(a.split('/'))
    res = (int(b[0])/int(b[1]))
    return res

def result(x):
    """вычисление 
    """
    if x in integer:
        return int(x)
    elif x not in integer and len(x) > 4:
        new_x = x.split(' ')
        a = int(new_x[0])
        b = nam_fact(new_x[1])
        if a < 0:
            c = a - b
            return c
        else:
            c = a + b
            return c
    elif len(x) >= 3:
        d = nam_fact(x)
        return d
    else:
        x = int(x)
        return x

def my_round(number, n=2):
    """округляем десятичное
    """
    ndigits = 10**n
    number = int(number * ndigits) / ndigits
    return number

def lcm(a, b):
    """Наименьшее общее кратное
    """
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a, b

def decim_to_fract(b):
    """перевод из десятичных в дроби
    """
    if b >= 10:
        numb = 100
    else:
        numb = 10

    l = lcm(b, numb)
    list_fil = list(filter(lambda num: num != 0, l))
    num = list_fil[0]
    new_num_1 = int(b/num)
    new_num_2 = int(numb/num)
    return new_num_1, new_num_2

def get_numbers(res):
    """получение дробного числа
    """
    my_num = str(my_round(res))
    equ_1, equ_2 = map(float, my_num.split(".", 1))
    return equ_1, equ_2

if minus in expression:
    equ = expression.split(minus)
    lst_1.append(equ[0])
    lst_2.append(equ[1])

elif plus in expression:
    equ = expression.split(plus)
    lst_1.append(equ[0])
    lst_2.append(equ[1])

def new_res(x):
    """вывод результата
    """
    if x[0] == 0.0 and x[1] == 0.0:
        print("Вывод: {}".format(int(x[0])))
    elif x[0] == 0.0:
        k = str(x[0])
        k_1, k_2 = map(str, k.split(".", 1))
        if "-" in k_1:
            b = decim_to_fract(x[1])
            print("Вывод: -{}/{}".format(b[0], b[1])) 
        else:
            b = decim_to_fract(x[1])
            print("Вывод: {}/{}".format(b[0], b[1])) 
    elif x[1] == 0.0:
        print("Вывод: {}".format(int(x[0])))
    else:
        b = decim_to_fract(x[1]) 
        print("Вывод: {} {}/{}".format(int(x[0]), b[0], b[1])) 

# **************************************************************
if minus in expression:
    result_1 = result(lst_1[0])
    result_2 = result(lst_2[0])

    new_result = result_1 - result_2
    get_numbers(new_result)
    new_my_num = get_numbers(new_result)
    new_res(new_my_num)

elif plus in expression:
    result_1 = result(lst_1[0])
    result_2 = result(lst_2[0])
    new_result = result_1 + result_2

    get_numbers(new_result)
    new_my_num = get_numbers(new_result)
    new_res(new_my_num)

else:
    print("Не правильно ввели оператор")
