# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School():
    def __init__(self, school_name, town, teachers, pupils):
        self.school_name = school_name
        self.town = town
        self.teachers = teachers
        self.pupils = pupils 

    def get_school_classes(self):
        all_classes=[]
        for pupil in self.pupils:
            all_classes.append(pupil.get_school_class()) 
        all_classes = sorted(set(all_classes))
        return all_classes

    def get_list_pupils_from_class(self, school_class):
        list_class = []
        for pupil in self.pupils:
            if school_class == pupil.get_school_class():
                list_class.append(pupil.get_full_name())

        str_list_class = (str(list_class).replace("[", "").replace("]", "").replace("'", ""))
        print("Класс {}: {}".format(school_class, str_list_class))

    def get_pupils(self):
        for pupil in self.pupils:
            return pupil.get_full_name()

    def get_list_object_pupil(self, full_name):
        for pupil in self.pupils:
            if full_name == pupil.get_full_name():
                print(full_name)
                class_pupil = pupil.get_school_class()

        for teacher in self.teachers:
            if class_pupil in teacher.get_class():
                print("Учитель: {}, Предмет: {}".format(teacher.get_full_name(), teacher.get_object_name()))             

    def get_parents_pupil(self, full_name):
        for pupil in self.pupils:
            if full_name == pupil.get_full_name():
                parents = pupil.get_parents()
                print(full_name, parents)

    def get_all_teachers_in_school_class(self, school_class):
        list_teacher = []
        for teacher in self.teachers:
            if school_class in teacher.get_class():
                list_teacher.append(teacher.get_full_name())
        
        str_list_teach = (str(list_teacher).replace("[", "").replace("]", "").replace("'", ""))
        print ("Все учителя класса {}: {}".format(school_class, str_list_teach))

class Person:
    def __init__(self, last_name, first_name, midl_name,):
        self.f_name = first_name
        self.m_name = midl_name
        self.l_name = last_name

    def get_full_name(self):
        return "{} {} {}".format(self.l_name, self.f_name[:1] + ".", self.m_name[:1]+ ".")

class Pupil(Person):
    def __init__(self, first_name, midl_name, last_name, school_class, mather, father):
        super().__init__(first_name, midl_name, last_name)
        self.school_class = school_class
        self.parents = {"Мама:":mather, "Папа:":father}

    def get_parents(self):
        return self.parents

    def get_school_class(self):
        return self.school_class

class Teacher(Person):
    def __init__(self, first_name, midl_name, last_name, object_name, school_class):
        super().__init__(first_name, midl_name, last_name)
        self.object_name = object_name
        self.school_class = school_class

    def get_object_name(self):
        return self.object_name

    def get_class(self):
        return self.school_class


if __name__ == "__main__":

    teachers = [Teacher('Иванов', 'Иван', 'Иванович', 'Математика', ['7А', '8А']),
                Teacher('Петров', 'Петр', 'Петрович', 'История', ['7А', '8А']),
                Teacher('Гранова', 'Аглая', 'Федоровна', 'Геграфия', ['7А', '8Б']),
                Teacher('Грачева', 'Светлана', 'Владимирована', 'Природоведение', ['1А', '3A']),
    ]

    pupils = [Pupil('Борисов', 'Борис', 'Борисович', '2А', 'Борисова А.В.', 'Борисов Б.А.'),
            Pupil('Наумов', 'Петр', 'Дмитриевич', '2А', 'Наумова А.В.', 'Наумов Д.А.'),
            Pupil('Сидоров', 'Дмитрий', 'Витальевич', '3А', 'Сидоров А.В.', 'Сидоров В.А.'),
            Pupil('Пушкина', 'Виктория', 'Евгеньевна', '7А', 'Пушкина Г.В.', 'Пушкин Е.А.'),
            Pupil('Васильев', 'Василий', 'Васильевич', '7А', 'Калинина Г.В.', 'Калинин А.А.'),
            Pupil('Рузамовская', 'Варвара', 'Евгеньевна', '7А', 'Рузамовская Е.В.', 'Рузамовский Е.А.'),
            Pupil('Калинина', 'Евгения', 'Александровна', '8Б', 'Калинина Г.В.', 'Калинин А.А.'),
            Pupil('Федоров', 'Александр', 'Витальевич', '8Б', 'Федорова Г.В.', 'Федоров В.А.'),
    ]

    school = School('Начальная школа №1', 'Тольятти', teachers, pupils)

    print(school.school_name)
    print(school.town)
    print("")

    # 1. Получить полный список всех классов школы
    list_classes = ', '.join(school.get_school_classes())
    print("Полный список всех классов школы: {}".format(list_classes))
    print("")

    # 2. Получить список всех учеников в указанном классе
    #  (каждый ученик отображается в формате "Фамилия И.О.")
    school.get_list_pupils_from_class('8Б')
    print("")

    # 3. Получить список всех предметов указанного ученика 
    #  (Ученик --> Класс --> Учителя --> Предметы)
    school.get_list_object_pupil('Пушкина В. Е.')
    print("")

    # 4. Узнать ФИО родителей указанного ученика
    school.get_parents_pupil('Федоров А. В.')
    # print("")

    # 5. Получить список всех Учителей, преподающих в указанном классе
    school.get_all_teachers_in_school_class('8А')
