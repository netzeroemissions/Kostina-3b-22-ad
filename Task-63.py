class ProductCard:
    def __init__(self, name, price, qt):
        self.name = name
        self.price = price
        self.qt = qt

    def qt_decrease(self, qt_sold):
        if self.qt >= qt_sold:
            self.qt -= qt_sold
        else:
            print(f'Доступно только {self.qt} штук')

    def price_change(self, new_price):
        if new_price <= 0:
            print('Цена не может быть отрицательной либо равной нулю')
        else:
            self.price = new_price

sku_1 = ProductCard('Шоколад', 150, 1)
sku_1.qt_decrease(8)
sku_1.price_change(-10)

print(sku_1.name, sku_1.qt, 'шт.', sku_1.price, 'руб.')