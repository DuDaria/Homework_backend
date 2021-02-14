# -ПРЕДПРИЯТИЕ----------------------------------------------------
class Enterprise:
    def __init__(self, name, town):
            self.name = name
            self.town = town
            self.employees = []
            self.positions = [] 
            self.all_id = []
            self.subdiv_control = Control(self.put_all_employees())
            self.hum_res_dep = HumanResourcesDepartment(self.put_all_employees())
            self.bookkeep = Bookkeeping(self.put_all_employees())
            self.prod = Production(self.put_all_employees())

    def hire_employee(self, people, position):
        """нанимаем сотрудника на работу"""
        self.employee = []
        self.employee.append(people.get_full_name())
        self.employee.append(people._birthday)
        self.employee.append(people._phone)
        self.employee.append(position)
        self.positions.append(position)
        self.employee.append(self.add_code_and_sallary(position))
        self.employees.append(self.employee)
        return self

    def fire_employee(self, position, id):
        """увольняем сотрудника с работы"""
        for emploe in self.employees:
            for i in emploe:
                if position == i and id == emploe[-1]:
                    print("Сотрудник уволен!")
                    self.employees.remove(emploe)
                    self.positions.remove(position)
                else:
                    pass

    def get_all_employees(self):
        """получить всех сотрудников"""
        for pupil in self.employees:
            print(f"Сотрудник: {pupil}")

    def get_emploee_in_position(self, position):
        """получить сотрудника по позиции"""
        for emploe in self.employees:
            for i in emploe:
                if position == i:
                    print(emploe)

    @staticmethod
    def add_code_and_sallary(position):
        """добавляем зарплату и код"""
        if position == "Директор":
            code_depart = 100
            sallary = 80000
            return f"code_dep = {code_depart}", f"sallary = {sallary}"
        if position == "Бухгалтер":
            code_depart = 20
            sallary = 50000
            return f"code_dep = {code_depart}", f"sallary = {sallary}"
        if position == "Кадровик":
            code_depart = 10
            sallary = 50000
            return f"code_dep = {code_depart}", f"sallary = {sallary}"
        if position == "Менеджер по продукции":
            code_depart = 30
            sallary = 30000
            return f"code_dep = {code_depart}", f"sallary = {sallary}"
        if position == "":
            raise ValueError

    def add_id(self):
        """добавляем идентификатор"""
        num = 0
        for emploe in self.employees:
            num += 1
            emploe.append(f"id = {num}")

    def put_all_employees(self):
        return self.employees

    def get_all_Control(self):
        """получаем все об отделе Управления"""
        name = self.subdiv_control._name
        code_dep = self.subdiv_control._code
        employers = self.subdiv_control.add_empl()
        return name, f"Код отдела: {code_dep}", f"Сотрудники:{employers}"
    
    def get_all_HumResDep(self):
        """получаем все об отделе Кадров"""
        name = self.hum_res_dep._name
        code_dep = self.hum_res_dep._code
        employers = self.hum_res_dep.add_empl()
        return name, f"Код отдела: {code_dep}", f"Сотрудники:{employers}"

    def get_all_Bookkeeping(self):
        """получаем все об отделе Бухгалтерии"""
        name = self.bookkeep._name
        code_dep = self.bookkeep._code
        employers = self.bookkeep.add_empl()
        return name, f"Код отдела: {code_dep}", f"Сотрудники:{employers}"

    def get_all_Production(self):
        """получаем все об отделе Продукции"""
        name = self.prod._name
        code_dep = self.prod._code
        employers = self.prod.add_empl()    
        return name, f"Код отдела: {code_dep}", f"Сотрудники:{employers}"


class Department:
    def __init__(self, *args):
        self.args = args

    def add_empl(self):
        employees = []
        for i in self.args:
            for b in i:
                for x in b[4]:
                    if x == f'code_dep = {self._code}':
                        employees.append(b)
        return employees


# --ОТДЕЛ УПРАВЛЕНИЯ-----------------------
class Control(Department):
    _name = "Отдел управления предприятием"
    _code = 100


# --ОТДЕЛ КАДРОВ----------------------------
class HumanResourcesDepartment(Department):
    _name = "Отдел кадров"
    _code = 10


# --БУХГАЛТЕРИЯ -----------------------------
class Bookkeeping(Department):
    _name = "Бухгалтерия"
    _code = 20


# --ПРОДУКЦИЯ--------------------------------
class Production(Department):
    _name = "Отдел Продукции"
    _code = 30


class Person:
    def __init__(self, last_name, first_name, midl_name, birthday, phone):
        self._l_name = last_name
        self._f_name = first_name
        self._m_name = midl_name
        self._birthday = birthday
        self._phone = phone

    def get_full_name(self):
        return "{} {} {}".format(self._l_name, self._f_name[:1] + ".", self._m_name[:1]+ ".")

    def get_birthday(self):
        return self._birthday

    def get_phone(self):
        return self._phone

if __name__ == "__main__":
    
    enterprise = Enterprise('ОАО ЗВЕЗДА', 'г.Тольятти')
    print(enterprise.name, enterprise.town)
    # Нанять сорудника на должность
    new_person1 = Person('Здоровяк', 'Олег', 'Александрович', '01.01.1963', '8-800-2000-600')
    enterprise.hire_employee(new_person1, 'Директор')
    new_person2 = Person('Сидоров', 'Федр', 'Инокентьевич', '01.01.1975', '8-800-2050-600')
    enterprise.hire_employee(new_person2, 'Кадровик')
    new_person3 = Person('Иванов', 'Иван', 'Иванович', '01.01.1985', '8-800-2060-600')
    enterprise.hire_employee(new_person3, 'Бухгалтер')
    new_person4 = Person('Петров', 'Петр', 'Петрович', '01.01.1995', '8-800-2070-600')
    enterprise.hire_employee(new_person4, 'Менеджер по продукции')
    new_person4 = Person('Васечкин', 'Вася', 'Петрович', '01.01.2000', '8-800-2080-600')
    enterprise.hire_employee(new_person4, 'Менеджер по продукции')

    enterprise.add_id()
    enterprise.put_all_employees()

    # Получаем всех сотрудников
    enterprise.get_all_employees()
    print("")

    # Получаем сотрудника по позиции
    enterprise.get_emploee_in_position('Директор')
    print("")

    # Получаем все должности
    print(enterprise.positions)
    print("")

    # Получаем все об Отделе Управления
    print(enterprise.get_all_Control())
    print("")

    # Получаем все об Отделе Кадров
    print(enterprise.get_all_HumResDep())
    print("")

    # Получаем все об отделе Управления
    print(enterprise.get_all_Bookkeeping())
    print("")

    # Получаем все об отделе Управления
    print(enterprise.get_all_Production())

    print("")
    # Уволить сотрудника с должности
    enterprise.fire_employee('Менеджер по продукции', 'id = 4')
    print("")

    #Проверяем увольнение
    enterprise.get_all_employees()
    print("")

    # Проверяем сотрудника из отдела 
    print(enterprise.get_all_Production())
