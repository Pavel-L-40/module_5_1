class House:

    def __init__(self, name, floors):
        self.name = name
        self.numbers_of_floor = floors

    def go_too(self, new_floor):
        if self.numbers_of_floor <= new_floor or new_floor < 0:
            print(f'в {self.name} такого этажа не существует!')
        else: print(f'в {self.name} этаж есть')


alp = House('ЖК Эльбрус', 30)
alp.go_too(110)

fav = House('ЖК Фавторит', 50)
fav.go_too(110)

fav.numbers_of_floor = 120
fav.go_too(110)
