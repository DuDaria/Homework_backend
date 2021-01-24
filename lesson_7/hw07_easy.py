# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# Решение двух задач
import math

class Figure:
    def __init__(self, name, perimetr, square):
        self.name = name
        self.perim = perimetr
        self.sq = square

    def get_result(self):
        return f"Название фигуры: {self.name} \n" \
                f"Площадь: {self.sq} кв.см.\n" \
                f"Периметр: {self.perim} cм. \n"

class Triangle(Figure):
    #конструктор класса
    def __init__(self, A, B, C):
        # self.name = name
        self.A = A
        self.B = B
        self.C = C
        # print("Cоздан Треугольник!")


        def side_len(x, y):
            """Вычисление длины строны
            """
            return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
        
        #Вызов функции side_len и записывание в переменную
        self.AB = side_len(self.A, self.B)
        self.BC = side_len(self.B, self.C)
        self.CA = side_len(self.C, self.A)
    
    def get_name(self):
        self.name = "Треугольник"
        return self.name

    # Периметр треугольника
    def perim_triang(self):
        return self.AB + self.BC + self.CA

    # Площадь треугольника
    def square_triang(self):
        self.half_P = self.perim_triang() / 2
        return math.sqrt(self.half_P *(self.half_P-self.AB) * (self.half_P-self.BC) * (self.half_P-self.CA)) 

    # Высота треугольника
    def hight_triang(self):
        return (2*self.square_triang()) / self.AB
    
    def get_result(self):
        return f"Высота: {self.hight_triang()} см.\n"

class IsoscelesTrapezoid(Figure):
    #конструктор класса
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        # print("Cоздана Трапеция!")

        def side_len(x, y):
            """Вычисление длины строны
            """
            return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
        
        #Вызов функции side_len и записывание в переменную
        self.AB = side_len(self.A, self.B)
        self.BC = side_len(self.B, self.C)
        self.CD = side_len(self.C, self.D)
        self.DA = side_len(self.D, self.A)
    
    def get_side_len(self):
        return f"Длины строн: A={self.AB} см., B={self.BC} см., C={self.CD}, D={self.DA} см."

    def get_name(self):
        self.name = "Равнобедренная трапеция"
        return self.name
    
    # Периметр трапеции
    def perim_trap(self):
        return self.AB + self.BC + self.CD + self.DA

    # Площадь трапеции
    def square_trap(self):
        return ( (self.AB + self.CD)/2)*(math.sqrt(self.BC**2 - ((self.AB - self.CD)**2/4)) )


triangle = Triangle((3, 2), (1, 1), (1, 3))
trapezoid = IsoscelesTrapezoid((1, 1), (1, 5), (3, 4), (3, 2))
  
figure1 = Figure(triangle.get_name(), triangle.perim_triang(), triangle.square_triang())
figure2 = Figure(trapezoid.get_name(), trapezoid.perim_trap(), trapezoid.square_trap())

print(figure1.get_result() + triangle.get_result())
print(figure2.get_result() + trapezoid.get_side_len())
