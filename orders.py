from menus import get_menu_selection, display_selection_error
from pizzas import pizza

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

    def get_total_price(self):
        return sum(pizza.get_total_price() for pizza in self.pizzas)


    def add_pizza(self):
        pizza = Pizza.make_pizza()
        if pizza is not None:
            self.pizzas.append(pizza)
            print("\n Pizza added to cart!")

    def display_pizzas(self):
        if len(self.pizzas) == 0:
            print("There are no pizzas in cart")
        else:
            for index, pizza in enumerate (self.pizzas):
                print("\n{index}: Pizza {index:<10} ${price:,.2f}".format(index=index+1, pizza=price.get_total_price()))
            pizza.display_toppings()        

        print("")
        print("*"*40)
        print("Shopping Cart Total: ${:,.2f}".format(self.get_total_price()))

    def remove_pizzas(self):
        while True:
            self.display_pizzas()
            print("0: Cancel")
            menu_selection = input("\nPlease select a pizza to remove. ")

            if menu_selection == "0":
                break
            elif (menu_selection.isdigit()
                and int(menu_selection) -1 < len(self.pizzas)):

                pizza = self.pizzas[int(menu_selection) -1]
                self.pizzas.remove(pizza)
                print("\n{} removed from the cart.".format(menu_selection))
            else:
                display_selection_error(menu_selection)


    def display_menu(self):
        while True:
            menu_selection = get_menu_selection(self.MENU_ITEMS)

            if menu_selection == "0": 
                break
            elif menu_selection == "1":
                self.add_pizza()
            elif menu_selection == "2":
                self.display_pizzas()
            elif menu_selection == "3":
                self.remove_pizzas()
            elif menu_selection == "4":
                self.pizzas = []
            else:
                display_sel