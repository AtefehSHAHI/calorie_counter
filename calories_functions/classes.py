import json
import datetime
import calories_complex_data
import calories_price_counter
from exceptions import InvalidItems, TooMuchCalories

with open("data/meals.json") as file:
    meals = json.load(file)['meals']

with open("data/combos.json") as file:
    combos = json.load(file)['combos']

meal_dicts_id = {
    meal["id"]: meal
    for meal in meals
}

meal_dicts_name = {
    meal["name"]: meal
    for meal in meals
}

combo_dicts_name= {
    combo["id"]: combo
    for combo in combos
}

combo_dicts_name = {
    combo["name"]: combo
    for combo in combos
}

# Complete the `Order` class
# in a dedicated file,
# it must respect the
# information given in the
# docstring.

# An order can be refused if the total is more than 2000 calories or if an unknown item is ordered.


class Order:
    """
    This class represents an order.

    Arguments:
        items (list): A list of item ids.
        date (datetime): The date and time of the order.

    Class attributes:
        counter (int): A counter for the number of orders.

    Attributes:
        order_id (str): A unique identifier for the order.
        order_accepted (bool): Whether or not the order was accepted.
        order_refused_reason (str): The reason the order was refused.
        date (datetime): The date and time of the order.
        items (list): A list of item ids.

    Properties:
        calories (int): The total calories for the order.
        price (int): The total price for the order.
    """
    counter = 1

    def __init__(self, items, date=None):

        self.order_id = f"order-{Order.counter}"
        Order.counter += 1
        self.items = items
        self._calories = None
        self._price = None
        self.order_valid = False
        self.order_error_message = None

        if date is None:
            self.date = datetime.date.today()
        else:
            self.date = datetime.datetime.strptime(date, "%d-%b-%Y")
        try:
            self.calories
            self.price
        except (InvalidItems, TooMuchCalories) as message:
            self._calories = 0
            self._price = 0
            self.order_error_message = str(message)
        else:
            self.order_valid = True
            self.order_error_message = None

    @property
    def calories(self):
        if self._calories is None:
            self._calories = calories_complex_data.Total_Order(*self.items)
        return self._calories

    @property
    def price(self):
        if self._price is None:
            self._price = calories_price_counter.calculate_total_price(*self.items)
        return self._price
