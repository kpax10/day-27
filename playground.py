from os import makedev


def add(*args):
    return sum(args)
print(add(2,3,4))

def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs['add']
    n *= kwargs['multiply']

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs['make']
        self.model = kwargs['model']

my_car = Car(make='Ford', model='Fiesta')
print(my_car.make, my_car.model)