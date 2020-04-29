class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(5, 10)
print(point1.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'hi I am {self.name}')


john = Person('John Smith')
john.talk()

bob = Person('Bob Smith')
bob.talk()