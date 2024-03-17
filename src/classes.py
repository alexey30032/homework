from abc import ABC, abstractmethod
from mixin import MixinLog


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self, name, description, amount, quantity_in_stock):
        self.name = name
        self.description = description
        self.amount = amount
        self.quantity_in_stock = quantity_in_stock


    @abstractmethod
    def create_product(self, **kwargs):
        pass


class Category:
    """Класс категории"""
    name: str
    description: str
    goods: list

    total_numbers_of_category = 0
    unique_goods = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods

        Category.total_numbers_of_category += 1
        Category.unique_goods += len(goods)

    def goods_list(self, product):
        """Получает обьект Product на вход и добавляет его в список"""
        if isinstance(product, Product) or issubclass(product, Product):
            self.__goods.append(product.get_name, product.get_description,
                                product.get_price, product.get_quantity_in_stock)
        else:
            raise TypeError

    @property
    def get_goods(self):
        """Вывод информации по продуктам"""
        list_goods = []
        for item in self.__goods:
            list_goods.append(f'{item["name"]}, {item["price"]} руб. Остаток: {item["quantity_in_stock"]} шт.\n')
        return "".join(list_goods)

    def average_price(self):
        """подсчет среднего ценника всех товаров"""
        try:
            total_price = sum(Product.amount for amount in self.__goods)
            average_price = total_price / len(self.__goods)
        except ZeroDivisionError:
            return
        return average_price

    def __str__(self):
        return f'Категория: {self.name}, количество продуктов: {len(self.__goods)}'

    def __len__(self):
        return len(self.__goods)


class Product(BaseProduct, MixinLog):
    """Класс продукта"""

    name: str
    description: str
    amount: float
    quantity_in_stock: int

    def __init__(self, name, description, amount, quantity_in_stock):
        super().__init__(name, description, amount, quantity_in_stock)
        if self.quantity_in_stock == 0:
            print("Товар с нулевым количеством не может быть добавлен")
            raise ValueError
        print('Товар добавлен')

    @property
    def get_name(self):
        return self.name

    @property
    def get_description(self):
        return self.description

    @property
    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    @property
    def get_price(self):
        return self.amount

    @get_price.setter
    def price(self, new_price):
        if new_price <= 0 or new_price == self.get_price:
            print(f'Некорректное значение цены')
        elif new_price < self.get_price:
            while True:
                user_answ = input("Новая цена ниже чем старая, вы уверены что хотите изменить цену? "
                                  "(y/n): ").lower()
                if user_answ == 'y':
                    self.amount = new_price
                    break
                else:
                    self.amount = self.amount
                    break
        else:
            self.amount = new_price

    @classmethod
    def create_product(cls, **product):
        return cls(**product)

    def __str__(self):
        return f'{self.name}: {self.amount} руб. Остаток: {self.quantity_in_stock} шт.'

    def __add__(self, other):
        if type(self) == type(other):
            return self.amount * self.quantity_in_stock + other.amount * other.quantity_in_stock
        else:
            raise TypeError
