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

    def goods(self, product):
        """Получает обьект Product на вход и добавляет его в список"""
        self.__goods.append({"name": product[0],
                             "description": product[1],
                             "price": product[2],
                             "quantity_in_stock": product[3]})

    @property
    def get_goods(self):
        """Вывод информации по продуктам"""
        list_goods = []
        for item in self.__goods:
            list_goods.append(f'{item["name"]}, {item["price"]} руб. Остаток: {item["quantity_in_stock"]} шт.\n')
            return "".join(list_goods)


class Product:
    """Класс продукта"""
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, new_price):
        if new_price <= 0 or new_price == self.price:
            print(f'Некорректное значение цены')
        elif new_price < self.price:
            while True:
                user_answ = input("Новая цена ниже чем старая, вы уверены что хотите изменить цену? "
                                  "(y/n): ").lower()
                if user_answ == 'y':
                    self.price = new_price
                    break
                else:
                    self.price = self.price
                    break
        else:
            self.price = new_price

    @classmethod
    def create_product(cls, product):
        name, description, price, quantity_in_stock = (product["name"], product["description"],
                                                       product["price"], product["quantity_in_stock"])
        return cls(name, description, price, quantity_in_stock)
