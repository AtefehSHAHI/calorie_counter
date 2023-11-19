from exceptions import InvalidItems
'''meals = [
    {
        "id": "meal-1",
        "name": "hamburger",
        "calories": 600,
        "price": 5
    },
    {
        "id": "meal-2",
        "name": "cheese burger",
        "calories": 750,
        "price": 7
    },
    {
        "id": "meal-3",
        "name": "veggie burger",
        "calories": 400,
        "price": 6
    },
    {
        "id": "meal-4",
        "name": "vegan burger",
        "calories": 350,
        "price": 6
    },
    {
        "id": "meal-5",
        "name": "sweet potatoes",
        "calories": 230,
        "price": 3
    },
    {
        "id": "meal-6",
        "name": "salad",
        "calories": 15,
        "price": 4
    },
    {
        "id": "meal-7",
        "name": "iced tea",
        "calories": 70,
        "price": 2
    },
    {
        "id": "meal-8",
        "name": "lemonade",
        "calories": 90,
        "price": 2
    }
]

# Dictionary comprehension for meals
meals_dict = {meal["name"]: meal for meal in meals}

combos = [
    {
        "id": "combo-1",
        "name": "cheesy combo",
        "meals": [meals_dict["cheese burger"], meals_dict["sweet potatoes"], meals_dict["lemonade"]],
        "price": 11,
    },
    {
        "id": "combo-2",
        "name": "veggie combo",
        "meals": [meals_dict["veggie burger"], meals_dict["sweet potatoes"], meals_dict["iced tea"]],
        "price": 10,
    },
    {
        "id": "combo-3",
        "name": "vegan combo",
        "meals": [meals_dict["vegan burger"], meals_dict["salad"], meals_dict["lemonade"]],
        "price": 10,
    }
]'''
import json

with open("data/meals.json") as file:
	meals = json.load(file)['meals']

with open("data/combos.json") as file:
	combos = json.load(file)['combos']

# Dictionary comprehension for meals
meals_dict = {meal["name"]: meal for meal in meals}
# Dictionary comprehension for combos
combos_dict = {combo["name"]: combo for combo in combos}

# Calculate total calories for individual items using the meals_dict
def calculate_total_calories(*order):
    total_calories = 0
    for item in order:
        if item in meals_dict:
            total_calories += meals_dict[item]["calories"]
        else:
            print(f"Item '{item}' not found in the menu.")
    return total_calories

# Calculate total calories for a combo using the combos_dict
def combo_calorie_count(order):
    combo_menu = combos_dict.get(order, None)
    if combo_menu:
        combo_items = combo_menu["meals"]
        return sum(item["calories"] for item in combo_items)
    else:
        print(f"Combo '{order}' not found in the menu.")
        return 0

# Calculate total price for an order
def calculate_total_price(*order):
    total_price = 0
    for item in order:
        if item in meals_dict:
            total_price += meals_dict[item]["price"]
        elif item in combos_dict:
            total_price += combos_dict[item]["price"]
        else:
            ##print(f"Item '{item}' not found in the menu.")
            raise InvalidItems(item)
    return total_price

'''
# Merging the two functions to calculate total calories for a mixed order
def Total_Order(*Final_order):
    total_calories = 0
    for Food in Final_order:
        try:
            if Food in combos_dict:
                total_calories += combo_calorie_count(Food)
            elif Food in meals_dict:
                total_calories += meals_dict[Food]["calories"]
            else:
                print(f"Error: '{Food}' is not in any menus.")
        except KeyError:
            print(f"Error: '{Food}' is not in any menus.")
    return total_calories

'''



