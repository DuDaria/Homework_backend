import random as r


class Engine:
    def __init__(self, game):
        self.__game = game

    def play(self):
        choice = input("Поиграем в 'ЛОТО'? y/n: ")
        if choice == 'y':   
            self.__game.start()
        elif choice == 'n':
            print("Очень жаль что не удалось поиграть!")
            print("Программа завершена!")
        else:
            print("Неверное значение!")
            print("Программа завершена!")


class Game:

    @staticmethod
    def start(): 
        print("Игра началась!")
        barrels = Barrel.create_barrel()
        len_bar = len(barrels)
        print("Всего {} боченков".format(len_bar))
        user = Card.card_person()
        # print(user)
        comp = Card.card_computer()
        i = 0
        new_barrels = []
        new_user = []
        new_comp = []
        try:
            while input("Выйти из игры 'q' если нет, то нажмите любую клавишу: ") != "q":
                while i < len(barrels):
                    new_barrels.append(barrels[i])
                    del barrels[i]
                    print("Выпал боченок № {}. Осталось {} боченков.".format(barrels[i], len(barrels)))
                    n = input("Зачеркнуть цифру? (y/n): ")
                    for x in user:
                        for y in x:
                            if n == "y" and y == barrels[i]:
                                x[x.index(y)] = '-'
                                new_user.append(user[i])

                    print("------ Ваша карточка ------")
                    for b in user:
                        test = (str(b).replace("[", "").replace("]", "").replace("''", "").replace(",", " ").replace("'-'", "-"))
                        print(test)

                    for x in comp:
                        for y in x:
                            if y == barrels[i]:
                                x[x.index(y)] = '-'
                                new_comp.append(comp[i])

                    print("----------------------------")
                    print("--- Карточка компьютера --- ")
                    for b in comp:
                        test = (str(b).replace("[", "").replace("]", "").replace("''", "").replace(",", " ").replace("'-'", "-"))
                        print(test)
                
        except ValueError:
            print ('Ошибка, не правильно введено значение!')
        except IndexError:
            print ('Ошибка, list index out of range!')

        print("Программа завершена!")


class Card:

    @staticmethod
    def create_card():
        card = r.sample(range(1, 91), 15)

        n = 5 
        list_card = ([card[i:i+n] for i in range(0,len(card),n)])

        l = ['', '', '', '']
        lst_card =[]

        for i in list_card:
            joinedlist = i + l
            r.shuffle(joinedlist)
            # Сортировка листа
            def one_sort_cryptic(lst):
                s = sorted(lst, key=lambda el: (isinstance(el, str), el))
                return [s.pop(-isinstance(el, str)) for el in lst]

            sort_lst = (one_sort_cryptic(joinedlist))
            lst_card.append(sort_lst)

            str_card = (str(sort_lst).replace("[", "").replace("]", "").replace("''", "").replace(",", " "))
            print(str_card)
        return lst_card

    def card_person():
        print("------ Ваша карточка ------")
        return Card.create_card()
        
    def card_computer():
        print("----------------------------")
        print("--- Карточка компьютера --- ")
        return Card.create_card()


class Barrel:
    # def __init__(self):
    #     self.list = [i for i in range(1, 91)]

    def create_barrel():
        # Для вывода боченков на экран по очереди
        barrels = [i for i in range(1, 91)]
        r.shuffle(barrels) 
        return barrels
    

if __name__ == '__main__':

    game = Game()
    start_game = Engine(game)
    start_game.play() # Начало игры
