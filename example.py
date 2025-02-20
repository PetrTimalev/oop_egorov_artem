class Building:
    def __init__(self, num: int):
        self.floor = [i for i in range(1, num + 2)]

    def __setitem__(self, fl, name):
        self.floor[fl] = name

    def __getitem__(self, fl):
        if type(self.floor[fl]) is int:
            return None
        return self.floor[fl]

    def __delitem__(self, fl):
        del self.floor[fl]


iron_building = Building(22)  # Создаем здание с 22 этажами
print(iron_building[22])
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])