# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    def num_fib (n, m):
        fib_1 = 1
        fib_2 = 1
        for i in range(n, m): 
            print(fib_1 + fib_2, end=" ")
            f = fib_1
            fib_1 = fib_2
            fib_2 = f + fib_1

    if n > m:
        pass
    elif n == 1:
        print(1, 1, end=" ")
        num_fib(n, m)
    elif n == 2:
        print(1, end=" ")
        num_fib(n, m)
    else:
        num_fib(n, m)

fibonacci(3, 10)
print("")

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    ''' Cортировка пузырьком'''
    for i in range(len(origin_list)):
        for j in range(len(origin_list)-i-1):
            if origin_list[j] > origin_list[j+1]:
                origin_list[j], origin_list[j+1] = origin_list[j+1], origin_list[j]
    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(" ")

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(lambda_func, array):
    result = []
    for i in array:
        if lambda_func(i):
            result.append(i)
    return result

numbers = [5, -5, 6, 7, 8, -9, -2, -3]

lst = list(my_filter(lambda x: x > 0, numbers))
print('lst =', lst )
# [5, 6, 7, 8]
Filter = list(filter(lambda x: x > 0, numbers))
print('filter =', Filter)
# [5, 6, 7, 8]
print("")

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# A1 = [1, 0]
# A2 = [2, 2]
# A3 = [4, 3]
# A4 = [3, 1]
# True

# A1 = [-1, -1]
# A2 = [-2, -3]
# A3 = [-4, -3]
# A4 = [-3, -1]
# True

A1 = [-2, -1]
A2 = [2, 1]
A3 = [5, 1]
A4 = [4, -1]
# False

def parall(A1, A2, A3, A4):
    """
    параллелограмм
    x1 + x3 = x2 + x4
    y1 + y3 = y2 + y4
    """
    if A1[0] + A3[0] == A2[0] + A4[0] and A1[1] + A3[1] == A2[1] + A4[1]:
        return True
    else:
        return False

print(parall(A1, A2, A3, A4))
