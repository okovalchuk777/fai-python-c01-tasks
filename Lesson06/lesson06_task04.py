class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print("Машина поехала.")

    def stop(self):
        return print("Машина остановилась.")

    def turnright(self):
        return print("Машина повернула направо.")

    def turnleft(self):
        return print("Машина повернула налево.")

    def show_speed(self):
        return print(f'Текущая скорость равна {self.speed} км/ч.')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return print(f'На данном участке дороги масимально допустимая скорость составляет 60 км/ч.\nМашина '
                         f'превысила ограничение по скорости на {self.speed - 60} км/ч. Водитель будет оштрафован.')
        else:
            return print(f'Скорость машины составляет {self.speed} км/ч.')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return print(f'На данном участке дороги масимально допустимая скорость составляет 40 км/ч.\nМашина '
                         f'превысила ограничение по скорости на {self.speed - 40} км/ч. Водитель будет оштрафован.')
        else:
            return print(f'Скорость машины составляет {self.speed} км/ч.')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def belongingtothepolice(self):
        if self.is_police:
            return print(f'Это полицейская машина.')
        else:
            return print(f'Это не полицейская машина.')


a = Car(70, 'red', 'AUDI', False)
town_car = TownCar(110, 'black', 'Lanos', False)
police_car01 = PoliceCar(90, 'white and blue', 'Dodge', True)
a.turnright()
a.show_speed()
town_car.show_speed()
police_car01.belongingtothepolice()
