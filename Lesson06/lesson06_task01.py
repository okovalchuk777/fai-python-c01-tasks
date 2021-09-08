from time import sleep


class TrafficLight:

    def __init__(self):
        self.__color = ['КРАСНЫЙ', 'ЖЁЛТЫЙ', 'ЗЕЛЁНЫЙ']

    def running(self):
        i = 0
        while i < 3:
            if i == 0:
                print(f'Стой. На светофоре горит {TrafficLight.__color[i]} цвет.')
                sleep(7)
            elif i == 1:
                print(f'Приготовься переходить дорогу. На светофоре горит {TrafficLight.__color[i]} цвет.')
                sleep(2)
            elif i == 2:
                print(f'Быстро переходи дорогу. На светофоре горит {TrafficLight.__color[i]} цвет.')
                sleep(7)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
