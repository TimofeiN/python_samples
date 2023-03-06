"""
Simple example of oop classes using.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'машина {self.name} поехала')

    def stop(self):
        print(f'машина {self.name} остановилась')

    def turn(self, direction):
        print(f'машина {self.name} повернула в направлении {direction}')

    def show_speed(self):
        print(f'скорость = {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'превышена скорость')
        else:
            print(f'скорость = {self.speed}')


t = TownCar(56, 'red', 'lexus')
t.go()
t.turn('left')
t.stop()
t.show_speed()

second_t = TownCar(61, 'white', 'mazda')
second_t.show_speed()
