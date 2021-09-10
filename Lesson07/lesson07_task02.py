from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    @abstractmethod
    def fabric_consumption(self):
        pass

    @property
    def fabric_consumption(self):
        quantity = float((self.size / 6.5 + 0.5) + (self.growth * 2 + 0.3))
        return f'Для изготовления пальто и костюмов необходимо {quantity:.2f} кв.м. материала.'


class Coat(Clothes):
    def __init__(self, size, growth=None):
        super(Coat, self).__init__(size, growth)

    @property
    def fabric_consumption(self):
        quantity = float(self.size / 6.5 + 0.5)
        return f'Для изготовления пальто необходимо {quantity:.2f} кв.м. материала.'


class Suit(Clothes):
    def __init__(self, growth, size=None):
        super(Suit, self).__init__(size, growth)

    @property
    def fabric_consumption(self):
        quantity = float(self.growth * 2 + 0.3)
        return f'Для изготовления костюмов необходимо {quantity:.2f} кв.м. материала.'


clothes = Clothes(22, 15)
coat = Coat(22)
suit = Suit(15)
print(coat.fabric_consumption)
print(suit.fabric_consumption)
print(clothes.fabric_consumption)
