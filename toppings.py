class Topping():
    """
    What goes on pizza
    """

    def __init__(self, name, price=1.00):
        self.name = name 
        self.price = price 

    def __str__(self):
        return "{} ${:,.2f}".format(self.name, self.price)
