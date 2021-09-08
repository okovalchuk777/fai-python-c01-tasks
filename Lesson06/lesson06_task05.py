class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print(f'Запуск отрисовки.')


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print(f'{str(self.title).capitalize()} рисует мышку.')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print(f'{str(self.title).capitalize()} рисует кошку.')


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print(f'{str(self.title).capitalize()} рисует тигра.')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
pen.draw()
pencil.draw()
handle.draw()
