from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///hw16_(SQLAlchemy).db', echo = False)

Base = declarative_base()

class Sportsman(Base):
    __tablename__ = 'sportsmans'

    id = Column(Integer, primary_key=True)

    fullname = Column(String(), unique=True)
    rank = Column(String)
    year_of_birth = Column(Integer(), nullable=False)
    personal_record = Column(Integer)
    country = Column(String)

    def __init__(self, fullname, rank, year_of_birth, personal_record, country):
        self.fullname = fullname
        self.rank = rank
        self.year_of_birth = year_of_birth
        self.personal_record = personal_record
        self.country = country
    
    def __repr__(self):
        return "%s, %s, %s, %s, %s" % (self.fullname, self.rank,
        self.year_of_birth, self.personal_record, self.country)

class Competition(Base):
    __tablename__ = 'competitions'

    id = Column(Integer(), primary_key=True)
    name = Column(String)
    world_record = Column(String)
    set_date = Column(String)

    def __init__(self, name, world_record, set_date):
        self.name = name
        self.world_record = world_record
        self.set_date = set_date
    
    def __repr__(self):
        return "Competition(%s, %s, %s)" % (self.name, self.world_record, self.set_date)

class ResultCompetition(Base):
    __tablename__ = 'result_competitions'

    id = Column(Integer(), primary_key=True)
    competition_id = Column(Integer(), ForeignKey('competitions.id'))
    sportsman_id = Column(Integer(), ForeignKey('sportsmans.id'))
    result = Column(Integer) 
    city = Column(String)
    hold_date = Column(String)

    def __init__(self, competition_id, sportsman_id, result, city, hold_date):
        self.competition_id = competition_id
        self.sportsman_id = sportsman_id
        self.result = result
        self.city = city
        self.hold_date = hold_date

    def __repr__(self):
        return "'%s', '%s', '%s'" % (self.result, self.city, self.hold_date)

class ResultSportsman(Base):
    __tablename__ = 'result_sportsmans'
    id = Column(Integer(), primary_key=True)
    competition_id = Column(Integer(), ForeignKey('competitions.id'))
    sportsman_id = Column(Integer(), ForeignKey('sportsmans.id'))
    result = Column(Integer)
    city = Column(String)
    hold_date = Column(String)

# Создание таблиц
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Добавление элементов
sportsman_1 = Sportsman('Ivan Ivanov', 'кандидат в мастера спорта', 1990, 15, 'Russia')
sportsman_2 = Sportsman('Sidorov Semen', 'кандидат в мастера спорта', 1990, 18, 'Russia')
sportsman_3 = Sportsman('Petrov Aleks', 'первый спортивный разряд', 2000, 26, 'Russia')
sportsman_4 = Sportsman('Smirnov Georg', 'первый спортивный разряд', 2000, 27, 'Russia')
sportsman_5 = Sportsman('Igor Svetlov', 'кандидат в мастера спорта', 1990, 10, 'Russia')
sportsman_6 = Sportsman('Michael Shum', 'кандидат в мастера спорта', 1990, 12, 'Russia')
sportsman_7 = Sportsman('Ignat Ponomarev', 'кандидат в мастера спорта', 1991, 11, 'Russia')

session.add(sportsman_1)
session.add(sportsman_2)
session.add(sportsman_3)
session.add(sportsman_4)
session.add(sportsman_5)
session.add(sportsman_6)
session.add(sportsman_7)

competition_1 = Competition('Бег на 100 метров', '10 sec.', '12-05-2010')
competition_2 = Competition('Метание ядра', '25 m', '12-05-2010')
competition_3 = Competition('Прыжки в длину', '6.7 m', '15-05-2010')
competition_4 = Competition('Прыжки в высоту', '2 m', '15-05-2010')

session.add(competition_1)
session.add(competition_2)
session.add(competition_3)
session.add(competition_4)

result_competition_1 = ResultCompetition(2, 1, 15, 'Moscow', '12-05-2010')
result_competition_2 = ResultCompetition(1, 5, 10, 'Moscow', '12-05-2010')
result_competition_3 = ResultCompetition(1, 6, 11, 'Moscow', '12-05-2010')
result_competition_4 = ResultCompetition(1, 7, 12, 'Moscow', '12-05-2010')
result_competition_5 = ResultCompetition(2, 2, 15, 'Togliatty', '15-05-2010')
result_competition_6 = ResultCompetition(2, 3, 20, 'Togliatty', '15-05-2010')
result_competition_7 = ResultCompetition(2, 4, 22, 'Togliatty', '15-05-2010')
result_competition_8 = ResultCompetition(1, 2, 10, 'Togliatty', '15-05-2010')
result_competition_9 = ResultCompetition(3, 3, 5, 'Togliatty', '15-05-2010')
result_competition_10 = ResultCompetition(3, 4, 3, 'Togliatty', '15-05-2010')

session.add(result_competition_1)
session.add(result_competition_2)
session.add(result_competition_3)
session.add(result_competition_4)
session.add(result_competition_5)
session.add(result_competition_6)
session.add(result_competition_7)
session.add(result_competition_8)
session.add(result_competition_9)
session.add(result_competition_10)

session.commit()

def new_table():
    for item in session.query(ResultCompetition).order_by(ResultCompetition.result): 
        new_tab = ResultSportsman()
        new_tab.competition_id = item.competition_id
        new_tab.sportsman_id = item.sportsman_id
        new_tab.result = item.result
        new_tab.city = item.city
        new_tab.hold_date = item.hold_date
        session.add(new_tab) 
    session.commit()
new_table()

# Закрываем соединение с базой данных
session.close()

if __name__ == "__main__":
    # Получаем данные **************************************************
    # 3. Выдайте всю информацию о спортсменах из таблицы sportsman.
    for row in session.query(Sportsman, Sportsman.fullname).all(): 
        print (row.Sportsman) 
    print("")

    # #  4. Выдайте наименование и мировые результаты по всем соревнованиям.
    for instance in session.query(Competition, Competition.name, Competition.world_record): 
        print ("%s - %s" % (instance.name, instance.world_record))
    print("")

    # #  5. Выберите имена всех спортсменов, которые родились в 1990 году.
    for item in session.query(Sportsman, Sportsman.fullname, Sportsman.year_of_birth). \
    filter(Sportsman.year_of_birth == 1990):
        print ("%s - %s" % (item.fullname, item.year_of_birth))
    print("")

    # 6. Выберите наименование и мировые результаты по всем соревнованиям, 
    # установленные 12-05-2010 или 15-05-2010.
    for item in session.query(Competition, Competition.name, Competition.world_record, Competition.set_date). \
    filter(Competition.set_date == '15-05-2010'):
        print ("%s - %s - %s" % (item.name, item.world_record, item.set_date))
    print("")

    # 7. Выберите дату проведения всех соревнований, проводившихся в Москве 
    # и  полученные на них результаты равны 10 секунд.
    for item in session.query(ResultCompetition, ResultCompetition.hold_date, 
    ResultCompetition.city, ResultCompetition.result). \
    filter(ResultCompetition.result == 10, ResultCompetition.city == 'Moscow'):
        print ("%s - %s - %s" % (item.hold_date, item.city, item.result))
    print("")

    # #  8. Выберите имена всех спортсменов, у которых персональный рекорд менее 25 с.
    for item in session.query(Sportsman, Sportsman.fullname, Sportsman.personal_record). \
    filter(Sportsman.personal_record < 25):
        print ("%s - %s" % (item.fullname, item.personal_record))


    # 9. Создать таблицу как результат выполнения команды SELECT (result_competition 
    # сортировка по результатам) и вывод на экран созданной таблицы
    for item in session.query(ResultSportsman, ResultSportsman.city, 
    ResultSportsman.result, ResultSportsman.hold_date): 
        print ("%s - %s - %s" % (item.result, item.city, item.hold_date)) 
