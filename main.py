class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.go_to()
    def go_to(self, new_floor=0):
        if new_floor >= 1:
            if new_floor <= self.number_of_floors:
                for i in range(new_floor):
                    print(i + 1)
            else:
                print('Такого этажа не существует')

h1 = House('ЖК Горький', 18)
h2 = House('Домик в деревне', 2)
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
h1.go_to(5)
h2.go_to(10)
