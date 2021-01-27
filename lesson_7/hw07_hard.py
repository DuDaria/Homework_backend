# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os

class Job:
    def __init__(self, job_name, workers, hours_of):
        self.job_name = job_name
        self.workers = workers
        self.hours_of = hours_of 

    def sallary_worker(self):   
        for hours in self.hours_of:
            for worker in self.workers:
                if worker.l_name == hours.l_name:
                    if int(worker.hour_rate) < int(hours.work_hours):
                        # стоимость часа
                        cost_hour = int(worker.salary) / int(worker.hour_rate)

                        # переработка часов
                        sallary_hours = (int(hours.work_hours) - \
                                        int(worker.hour_rate))*(cost_hour*2)

                        # Расчет зарплаты за месяц
                        sallary_in_month = ((int(worker.salary) * int(hours.work_hours)) / \
                                                int(worker.hour_rate)) + sallary_hours
                        
                        print("Сотрудник переработавший норму:")
                        print(f"Фамилия и Имя: {worker.get_full_name()} \n" \
                              f"Должность: {worker.get_position()} \n" \
                              f"Зарплата (руб.): {worker.get_sallary()} \n" \
                              f"Норма_часов: {worker.get_hour_rate()}\n"\
                              f"Отработано_часов: {hours.get_work_hours()} \n"\
                              f"Зарплата_в_этом_месяце (руб.): {int(sallary_in_month)}\n"
                            )

                    elif worker.hour_rate >= hours.work_hours:
                        sallary_in_month = (int(worker.salary) * int(hours.work_hours)) / \
                                            int(worker.hour_rate)

                        print(f"Фамилия и Имя: {worker.get_full_name()} \n" \
                              f"Должность: {worker.get_position()} \n" \
                              f"Зарплата (руб.): {worker.get_sallary()} \n" \
                              f"Норма_часов: {worker.get_hour_rate()}\n"\
                              f"Отработано_часов: {hours.get_work_hours()} \n"\
                              f"Зарплата_в_этом_месяце (руб.): {int(sallary_in_month)}\n"
                            )
                else:
                    False


class Worker():
    def __init__(self, first_name, last_name, salary, position, hour_rate):
        self.f_name = first_name
        self.l_name = last_name
        self.salary = salary
        self.position = position
        self.hour_rate = hour_rate

    def get_full_name(self):
        self.full_name = "{} {}".format(self.l_name, self.f_name)
        return self.full_name

    def get_sallary(self):
        return self.salary
        
    def get_position(self):
        return self.position
    
    def get_hour_rate(self):
        return self.hour_rate


class HourseOf (Worker):
    def __init__(self, first_name, last_name, work_hours):
        self.f_name = first_name
        self.l_name = last_name
        self.work_hours = work_hours

    def get_l_name(self):
        return self.l_name_h

    def get_work_hours(self):
        return self.work_hours

# ***************************************************************
path = os.path.join('data', 'workers')
path_1 = os.path.join('data', 'hours_of')


with open(path, 'r', encoding='UTF-8') as w:
    lines = w.readlines()
    list_workers = []

    for line in lines[1:]:
        line_worker = line.split()
        list_workers.append(line_worker)


with open(path_1, 'r', encoding='UTF-8') as h:
    lines = h.readlines()
    list_hours = []

    for line in lines[1:]:
        line_hours = line.split()
        list_hours.append(line_hours)


hours_of = []
for i in list_hours:
    hours_of.append(HourseOf(i[0], i[1], i[2]))


workers = []
for i in list_workers:
    workers.append(Worker(i[0], i[1], i[2], i[3], i[4]))


if __name__ == "__main__":

    job = Job("ООО 'ОРИОН'", workers, hours_of)
    print(job.job_name)
    job.sallary_worker()
