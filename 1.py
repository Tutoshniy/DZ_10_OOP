class Animal:
    def __init__(self, weight, size):
        self.weight = weight
        self.size = size


class Bird(Animal):
    species = 'Bird'

    def __init__(self, age=1, food='seed', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.age = age
        self.food = food


class Fish(Animal):
    species = 'Fish'

    def __init__(self, age=1, food='algae', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.age = age
        self.food = food


class Insects(Animal):
    species = 'Insects'

    def __init__(self, age=1, food='green leaves', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.age = age
        self.food = food


class Bird_Factory(Bird):
    def create(self, size, weight, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = size
        self.weight = weight
        return Bird(size, weight)


example1 = Bird_Factory(size='small', weight=2)
print(f'{example1.species = }, {example1.food = }, {example1.size = }, {example1.age = }, {example1.weight = }')
