#!/usr/bin/env python3

from product_sales import Product, Sales
import random


product_data: list[tuple] = [
    ("widgetA", 5.99, 100),
    ("widgetB", 10.99, 100),
    ("widgetC", 14.99, 200),
    ("widgetD", 16.99, 50),
    ("widgetE", 14.99, 125),
    ("widgetF", 11.99, 75),
    ("widgetG", 4.99, 200),
    ("widgetH", 17.99, 200),
    ("widgetI", 1.99, 300),
    ("widgetJ", 13.99, 50),
]

x = random.randint(1, 10)


def create_product_objects(data: list[tuple]) -> list[Product]:
    products = []
    for product in product_data:
        name, price, quant = product
        products.append(Product(name, price, quant))
    return products


def report_sales(product_list: list[Product]):
    sales = Sales()
    for index, product_elem in enumerate(product_list):
        if index % 2 == 0:
            rand_num = random.randint(1, 10)
            sales.add_sale(product_elem, rand_num)
    return sales.generate_report()


if __name__ == "__main__":
    batch1 = create_product_objects(product_data)
    print(report_sales(batch1))
