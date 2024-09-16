class House:

    def __init__(self, name, floors):
        self.name = name
        self.numbers_of_floor = floors

    def go_too(self, new_floor):
        if self.numbers_of_floor <= new_floor or new_floor < 0:
            print(f'в {self.name} {new_floor} этажа не существует!')
        else:
            print(self.name, end = ': ')
            for i in range(new_floor): print(i+1, end =' ')
            print()


alp = House('ЖК Эльбрус', 30)
alp.go_too(110)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_too(5)
h2.go_too(10)
