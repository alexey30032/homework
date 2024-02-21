class Category:
    """Класс категории"""
    name: str
    description: str
    goods: str

    total_numbers_of_category = 0
    unique_goods = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.total_numbers_of_category += 1
        Category.unique_goods = len(goods)


class Product:
    """Классы продукта"""
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock

