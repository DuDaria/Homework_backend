# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


import os
path = os.path.join('data', 'workers')
path_1 = os.path.join('data', 'hours_of')

with open(path, 'r', encoding='UTF-8') as w:
    lines = w.readlines()
    list_workers = []

    for line in lines[1:]:
        line_worker = line.split()
        list_workers.append(line_worker)

    workers= dict(zip(range(len(list_workers)), list_workers))

with open(path_1, 'r', encoding='UTF-8') as h:
    lines = h.readlines()
    list_hours = []

    for line in lines[1:]:
        line_hours = line.split()
        list_hours.append(line_hours)

    hours_of = dict(zip(range(len(list_hours)), list_hours))

# Выводим с помощью именованных аргументов
def conclusion(**kwargs):
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))

for i in hours_of:
    name_h = hours_of[i][0]
    surname_h = hours_of[i][1]
    work_in_h = int(hours_of[i][2])

    for i in workers:
        name_w = workers[i][0]
        surname_w = workers[i][1]
        sallary_w = int(workers[i][2])
        position_w = workers[i][3]
        hour_rate_w = int(workers[i][4])

        if surname_h == surname_w:
            print("")
            if hour_rate_w < work_in_h:
                # стоимость часа
                cost_hour = int(sallary_w / hour_rate_w)
                # переработка часов
                sallary_hours = int((work_in_h - hour_rate_w)*(cost_hour*2))
                # Расчет зарплаты за месяц
                sallary_in_month = ((int(sallary_w) * int(work_in_h))/int(hour_rate_w)) + sallary_hours

                print("Сотрудник переработавший норму:")
                conclusion(Имя=name_w, Фамилия=surname_w, Должность=position_w, Зарплата=sallary_w,  Норма_часов=hour_rate_w, Отработано_часов=work_in_h, Зарплата_в_этом_месяце=int(sallary_in_month))
            
            elif hour_rate_w > work_in_h:
                # Расчет зарплаты за месяц
                sallary_in_month = (sallary_w * work_in_h) / hour_rate_w
                conclusion(Имя=name_w, Фамилия=surname_w, Должность=position_w, Зарплата=sallary_w,  Норма_часов=hour_rate_w, Отработано_часов=work_in_h, Зарплата_в_этом_месяце=int(sallary_in_month))
        else:
            False
