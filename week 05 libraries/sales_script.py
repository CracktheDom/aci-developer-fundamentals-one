#!/usr/bin/env python3

from product_sales import Product, Sales
import random


def create_product_objects(data: list[tuple]) -> list[Product]:
    """
    Create a list of Product objects based on the provided data.

    Args:
    - data (list[tuple]): A list of tuples containing product information (
    name, price, quantity).

    Returns:
    - list[Product]: A list of Product objects.

    Note:
    - Each tuple in the data should have three elements: name (str), price (
    float), quantity (int).
    """
    products_list = []
    for product in product_data:
        name, price, quant = product
        products_list.append(Product(name, price, quant))
    return products_list


def report_sales(product_list: list[Product]) -> str:
    """
    Generate a sales report for a list of Product objects.

    Args:
    - product_list (list[Product]): A list of Product objects.

    Returns:
    - str: A formatted sales report.

    Note:
    - Sales are randomly generated for every second product in the list.
    """
    sales = Sales()  # create a Sales object

    # Iterate through product_list and generate random sales data
    for product_elem in product_list:
        rand_num = random.randint(1, 10)
        sales.add_sale(product_elem, rand_num)
    return sales.generate_report()


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


if __name__ == "__main__":
    # Create Product objects from the provided data
    batch1 = create_product_objects(product_data)

    # Generate and print a sales report for the created products
    print(report_sales(batch1))
