

import logging
logging.basicConfig(filename = 'file1.txt', level = logging.DEBUG, format = "%(asctime)s %(message)s" )
class shopping_cart :
    def __init__(self, name) :
        self.name = name
        self.__price = 0
    def adding_item(self, item_name, price):
        self.__price += price
        return (f"dear {self.name} your {item_name} is added. Thank You for using the cart.") 
    def removing_item(self, item_name, price):
        if price <= self.__price :
            self.__price -= price
            return f"dear {self.name} your {item_name} is remove. Thank You for using the cart."
        else:
            print("your enterd price is wrong. Thank You for using the Cart.")
    def your_price(self):
        return f"dear {self.name} your total price is: {self.__price}"
shopping_cart = shopping_cart('vishal')
logging.info(shopping_cart.adding_item('oil',200))
logging.info(shopping_cart.your_price())
logging.info(shopping_cart.adding_item('pen',5))
logging.info(shopping_cart.your_price())
