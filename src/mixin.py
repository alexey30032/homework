class MixinLog:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return (f'Создан обьект класса '
                f'{self.__class__.__name__}({self.name}, {self.description}, '
                f'{self.amount}, {self.quantity_in_stock})')


