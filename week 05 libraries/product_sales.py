#!/usr/bin/env python3


class Product:
    """
    This class represents a product with name, price, and inventory.
    """

    def __init__(self, name: str, price: float, inventory: int):
        """
        Initializes a Product instance.

        :param name: The name of the product.
        :param price: The price of the product.
        :param inventory: The initial inventory of the product.
        """
        self.name = name
        self.price = price
        self.inventory = inventory

    def __str__(self):
        """
        Returns a string representation of the product.

        :return: A string containing the name and price of the product.
        """
        return f"{self.name} (${self.price})"


class Sales:
    """
    This class manages sales data and generates reports.
    """

    def __init__(self):
        """
        Initializes a Sales instance with an empty list for sales data.
        """
        self.sales_data = list()

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.sales_data):
            raise StopIteration
        name = self.sales_data[self.index]["product"].name
        quantity = self.sales_data[self.index]["quantity"]
        sale = f"You sold {quantity} of {name}."
        self.index += 1
        return sale

    def add_sale(self, product: Product, quantity: int):
        """
        Adds a sale to the sales data list.

        :param product: The product being sold.
        :param quantity: The quantity of the product sold.
        """
        self.sales_data.append({"product": product, "quantity": quantity})

    def generate_report(self) -> str:
        """
        Generates a sales report based on the sales data.

        :return: A formatted string containing the sales report.
        """

        # Initialize variables
        total_revenue = 0
        unique_products = set()
        total_products_sold = {}

        # Iterate thru list of sales data
        for sale in self.sales_data:
            # Calculate total revenue
            total_revenue += float(
                sale["product"].__str__().split("$")[1].strip(")")
            ) * int(sale["quantity"])

            # Tabulate total products sold
            if sale["product"] not in total_products_sold:
                total_products_sold[sale["product"]] = sale["quantity"]
            else:
                total_products_sold[sale["product"]] += sale["quantity"]

            # Track unique products
            unique_products.update([sale["product"]])

        final_report = ""  # Initialize variable for final report

        # Iterate thru unique product list, tabulate total revenue and total
        # number sold for each product
        for unique_product in unique_products:
            # Generate report for each unique product
            final_report += f'# of {unique_product} units sold: {total_products_sold[unique_product]}, resulting in revenue of ${total_products_sold[unique_product] * float(unique_product.__str__().split("$")[1].strip(")")):,.2f}\n'

        # Add total revenue to the report
        final_report += (
            f"Total revenue for all products sold is ${total_revenue:,.2f}.\n"
        )
        return final_report


def test_classes():
    # Create Product instances
    prod1 = Product("WidgetA", 10.99, 100)
    prod2 = Product("WidgetB", 19.99, 50)
    prod3 = Product("WidgetC", 7.99, 150)
    prod4 = Product("WidgetD", 3.99, 500)
    prod5 = Product("WidgetE", 99.99, 500)

    # Create Sales instance
    sales = Sales()

    # Add sales data
    sales.add_sale(prod1, 15)
    sales.add_sale(prod2, 30)
    sales.add_sale(prod3, 45)
    sales.add_sale(prod1, 30)
    sales.add_sale(prod4, 100)
    sales.add_sale(prod5, 75)

    # Print the generated sales report
    print(sales.generate_report())

    # create iterator for Sales object
    sales_iter = sales.__iter__()

    # Iterate to next sales data item and display number of products sold
    print(next(sales_iter))
    print(next(sales_iter))
    print(next(sales_iter))
    print(next(sales_iter))
    print(next(sales_iter))


if __name__ == "__main__":
    test_classes()
