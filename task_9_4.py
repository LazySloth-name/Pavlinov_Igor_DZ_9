# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, name: str = 'bmw', speed: int = 0, color: str = 'red', is_police: bool = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print('автомобиль заведён')

    def stop(self):
        print('автомобиль остановился')

    def turn(self, direction: str):
        print(f'автомобиль поворачивает в {direction} направлении')

    def show_speed(self):
        print(f'скорость движения автомобиля : {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f'скорость движения: {self.speed} км/ч', '!!! превышение допустимой скорости' if self.speed > 60 else '')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'скорость движения: {self.speed} км/ч', '!!! превышение допустимой скорости' if self.speed > 40 else '')


class PoliceCar(Car):
    def __init__(self, name: str = 'audi', speed: int = 55, color: str = 'blue'):
        super().__init__(name, speed, color)
        self.is_police = True


tc = TownCar(speed=60)
tc.go()
tc.show_speed()
sc = SportCar()
sc.go()
sc.turn('разворот')
wc = WorkCar(speed=50)
wc.go()
wc.show_speed()
pc = PoliceCar()
pc.go()
pc.show_speed()
pc.stop()