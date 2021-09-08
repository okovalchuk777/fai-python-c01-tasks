class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        result = int(self._width)*int(self._length)*125/1000
        return result


a = Road(5000, 20)
print(a.asphalt_mass())

