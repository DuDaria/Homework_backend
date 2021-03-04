
import sqlite3

conn = sqlite3.connect('hw16.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute ("CREATE TABLE sportsman ( \
sportsman_id INTEGER PRIMARY KEY , \
sportsman_name TEXT,  \
sportsman_rank TEXT, \
year_of_birth INTEGER NOT NULL, \
personal_record INTEGER, \
country TEXT \
)")

cursor.execute ("CREATE TABLE competition ( \
competition_id INT NOT NULL, \
competition_name TEXT, \
world_record varchar(10), \
set_date varchar(15), \
PRIMARY KEY (competition_id) \
)")

cursor.execute ("CREATE TABLE result_competition ( \
competition_id INT REFERENCES competition(id), \
sportsman_id INT REFERENCES sportsman(id), \
result INTEGER NOT NULL, \
city TEXT, \
hold_date varchar(15), \
PRIMARY KEY (competition_id, sportsman_id) \
)")

# Запись в базу
# Вставляем данные в sportsman
cursor.execute("INSERT INTO sportsman VALUES (Null, 'Ivan Ivanov', 'кандидат в мастера спорта', 1990, 15, 'Russia')")
cursor.execute("INSERT INTO sportsman VALUES(Null, 'Sidorov Semen', 'кандидат в мастера спорта', 1990, 18, 'Russia')")
cursor.execute("INSERT INTO sportsman VALUES(Null, 'Petrov Aleks', 'первый спортивный разряд', 2000, 26, 'Russia')")
cursor.execute("INSERT INTO sportsman VALUES(Null, 'Smirnov Georg', 'первый спортивный разряд', 2000, 27, 'Russia')")
cursor.execute("INSERT INTO sportsman VALUES(Null, 'Igor Svetlov', 'кандидат в мастера спорта', 1990, 10, 'Russia')")
cursor.execute("INSERT INTO sportsman VALUES(Null, 'Michael Shum', 'кандидат в мастера спорта', 1990, 12, 'Russia')")
cursor.execute("INSERT INTO sportsman VALUES(Null, 'Ignat Ponomarev', 'кандидат в мастера спорта', 1991, 11, 'Russia')")

# # # Вставляем данные в competition
cursor.execute("INSERT INTO competition VALUES(10, 'Бег на 100 метров', '10 sec.', '12-05-2010')")
cursor.execute("INSERT INTO competition VALUES(20, 'Метание ядра', '25 m', '12-05-2010')")
cursor.execute("INSERT INTO competition VALUES(30, 'Прыжки в длину', '6.7 m', '15-05-2010')")
cursor.execute("INSERT INTO competition VALUES(40, 'Прыжки в высоту', '2 m', '15-05-2010')")

# # Вставляем данные в result_competition
cursor.execute("INSERT INTO result_competition VALUES(20, 1, 15, 'Moscow', '12-05-2010')")
cursor.execute("INSERT INTO result_competition VALUES(10, 5, 10, 'Moscow', '12-05-2010')")
cursor.execute("INSERT INTO result_competition VALUES(10, 6, 15, 'Moscow', '12-05-2010')")
cursor.execute("INSERT INTO result_competition VALUES(10, 7, 20, 'Moscow', '12-05-2010')")
cursor.execute("INSERT INTO result_competition VALUES(30, 2, 10, 'Togliatty', '15-05-2010')")
cursor.execute("INSERT INTO result_competition VALUES(40, 3, 15, 'Togliatty', '15-05-2010')")
cursor.execute("INSERT INTO result_competition VALUES(40, 4, 20, 'Togliatty', '15-05-2010')")

cursor.execute("CREATE TABLE result_sportsmans AS SELECT * FROM result_competition ORDER BY result")
# # сохраняем транзакцию
conn.commit()

# # Закрываем соединение с базой данных
conn.close()

if __name__ == "__main__":

    # Получаем данные из базы
    # 3. Выдайте всю информацию о спортсменах из таблицы sportsman.
    cursor.execute("SELECT * FROM sportsman")
    results = cursor.fetchall() 
    for result in results:
        print(result)
    print("") 

    # 4. Выдайте наименование и мировые результаты по всем соревнованиям.
    cursor.execute("SELECT competition_name, world_record FROM competition")
    results = cursor.fetchall() 
    for result in results:
        print(result)
    print("")

    # 5. Выберите имена всех спортсменов, которые родились в 1990 году.
    cursor.execute("SELECT sportsman_name, year_of_birth FROM sportsman WHERE year_of_birth = 1990")
    results = cursor.fetchall()
    for result in results:
        print(result)
    print("")

    # 6. Выберите наименование и мировые результаты по всем соревнованиям, 
    # установленные 12-05-2010 или 15-05-2010.
    cursor.execute("SELECT competition_name, world_record, set_date FROM competition WHERE set_date = '12-05-2010'")
    results = cursor.fetchall()
    for result in results:
        print(result)
    print("")

    # 7. Выберите дату проведения всех соревнований, проводившихся в Москве 
    # и  полученные на них результаты равны 10 секунд.
    cursor.execute("SELECT hold_date, city FROM result_competition WHERE city = 'Moscow' AND result = 10")
    results = cursor.fetchall() # только один раз выполняется 
    for result in results:
        print(result)
    print("")

    # 8. Выберите имена всех спортсменов, у которых персональный рекорд менее 25 с.
    cursor.execute("SELECT sportsman_name, personal_record FROM sportsman WHERE personal_record < 25")
    results = cursor.fetchall() 
    for result in results:
        print(result)
    print("")

    # 9. Создать таблицу как результат выполнения команды SELECT (result_competition 
    # сортировка по результатам) и вывод на экран созданной таблицы

    cursor.execute("SELECT * FROM result_sportsmans")
    results = cursor.fetchall() 
    for result in results:
        print(result)

