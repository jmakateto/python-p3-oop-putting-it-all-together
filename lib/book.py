class Book:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def is_in_stock(self):
        return self.quantity > 0
