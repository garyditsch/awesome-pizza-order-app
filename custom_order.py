def get_menu_selection(menu_items):
    """
    Display a menu and return the user's selection
    """
    print("\n")
    for menu_items in menu_items:
        print(menu_items)

    return input("\nPlease select an option from above.")

def get_menu_selection_error(menu_items):
    if menu_selection.isdigit():
        print("\n{} is an invalid option, please try again" .format(menu_selection))
    else:
        print("\n{} is not a number, please enter a number from the menu above" .format(menu_selection))

class Topping():
    """
    What goes on pizza
    """

    def __init__(self, name, price=1.00):
        self.name = name 
        self.price = price 


class Pizza():
    MENU_ITEMS = (
       "1: Add Toppings", 
       "2: Display Toppings",
       "3: Remove Toppings", 
       "4: Add Pizza to Cart",
       "0: Cancel",
    )

    AVAILABLE_TOPPINGS = (
        Topping("Cheese"), 
        Topping("Pepperoni", 2.00),
        Topping(name="Sausage", price=2.50)
    )



    def __init__(self):
        pass

    def __init__(self):
        self.toppings = []

    @classmethod
    def make_pizza(cls):
        """
        Return a new pizza based off what is entered by the user
        """

        #cls == Pizza
        pizza = cls()

        while True:
            menu_selection = get_menu_selection(pizza.MENU_ITEMS)

            if menu_selection == "0":
                return None
            elif menu_selection == "1":
                self.add_pizza()
            elif menu_selection == "4":
                return pizza 
            else:
                display_selection_error(menu_selection)

        return None

    def get_toppings_menu_list(self, toppings):
        menu_items = [
            "{}: {}".format(idex + 1, toppings)
            for index, toppings in enumerate(toppings)
        ]
        menu_items.append("0: Exit")

        return menu_items 

    def add_toppings(self):
        while True:
            menu_selection = get_menu_selection(
                self.get_toppings_menu_list(self.AVAILABLE_TOPPINGS)) 

            if menu_selection == "0":
                break

class Cart():
    MENU_ITEMS = (
       "1: Add Pizza to Order", 
       "2: Remove Pizza from Order",
       "3: Display Order", 
       "4: Order Pizza",
       "0: Exit",
    )

    def __init__(self):
        self.pizza = []

    def add_pizza(self):
        pizza = Pizza.make_pizza()
        if pizza is not None:
            self.pizzas.append(pizza)
            print("\n Pizza added to cart!")

    def display_menu(self):
        while True:
            menu_selection = get_menu_selection(self.MENU_ITEMS)

            if menu_selection == "0": 
                break
            if menu_selection == "1":
                self.add_pizza()


def main():
    """
    Main Loop
    """

    cart = Cart()
    cart.display_menu()

if __name__ == '__main__':
    main()