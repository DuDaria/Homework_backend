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
    def start(self): 
        print("Игра началась!")
        barrels = Barrel.create_barrel()
        print("Всего {} боченков".format(len(barrels)))
        self.user = Card.create_card()
        self.comp = Card.create_card()

        while True:
            self.card_user()
            self.card_comp()

            if self.result() == 0:
                barrel = barrels.pop()
                print("Выпал боченок № {}.\nОсталось {} боченков.".format(barrel, len(barrels)))
                choice = input("Для выхода нажмите 'q'.\nЗачеркнуть цифру? (y/n): ")

                if choice == 'y':
                    for x in self.user:
                        for y in x:
                            if y == barrel:
                                x[x.index(y)] = '-'

                elif choice == 'n':
                    pass
                elif choice == 'q':
                    print("Игра окончена!")
                    break
                else:
                    print("Вы ввели не правильное значение!")
                    print("Игра окончена!")
                    break
                
            elif self.result == 1:
                break
            elif self.result == 2:
                break
            elif self.result == 3:
                break
            else:
                break

            for x in self.comp:
                for y in x:
                    if y == barrel:
                        x[x.index(y)] = '-'    

    def card_user(self):
        print("------ Ваша карточка------")
        for b in self.user:
            test = (str(b).replace("[", "").replace("]", "").replace("''", "").replace(",", " ").replace("'-'", "-"))
            print(test)
        print("----------------------------")

    def card_comp(self):
        print("--- Карточка компьютера --- ")
        for b in self.comp:
            test = (str(b).replace("[", "").replace("]", "").replace("''", "").replace(",", " ").replace("'-'", "-"))
            print(test)
        print("----------------------------")

    def check(self, arg):
        """
        проверка для карточки
        """
        k = []
        for i in arg:
            for y in i:
                a = isinstance(y, (int))
                k.append(a)
        if True in k:
            return True
        else:
            return False

    def result(self):
        if self.check(self.user) == False:
            print("Поздравляю! Вы выйграли!")
            return 1
        elif self.check(self.comp) == False:
            print("Выйграл компьютер!")
            return 2
        elif self.check(self.user) == False and self.check(self.comp) == False:
            print("Ничья!")
            return 3
        else:
            return 0
            

class Card:
    @staticmethod
    def create_card():
        """
        создание карточки
        """
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

        return lst_card


class Barrel:
    @staticmethod
    def create_barrel():
        """
        создание боченков
        """
        barrels = [i for i in range(1, 91)]
        r.shuffle(barrels) 
        return barrels


if __name__ == '__main__':
    game = Game()
    start_game = Engine(game)
    start_game.play() # Начало игры
