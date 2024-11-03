print('Задача "Учёт товаров":')
from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        product = f'{self.name}, {self.weight}, {self.category}'
        return  product

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        for i in products:
            if (i.name in self.get_products()) and (str(i.weight) in self.get_products()):
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())