# #Part One
# #Create a calories counter function that can take either a list of meals OR an undefined number of meals (using *args).

calories = {
   'Hamburger': 600,
   'Cheese Burger': 750,
   'Veggie Burger': 400,
   'Vegan Burger': 350,
   'Sweet Potatoes': 230,
   'Salad': 15,
   'Iced Tea': 70,
   'Lemonade': 90,
}

# print(calories['Hamburger'])


def calculate_total_calories(*order):
    print(order)
    total_calories = 0
    for items in order:
        total_calories += calories [items]
    return (total_calories)





#Part Two
# Handling Combo:
# Start with a new dictionary:

combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
}

#define a separate function to calculate the combo options using the main function
def combo_calorie_count (order):
    combo_menu = combos [order]
    return (calculate_total_calories(*combo_menu))

# merging the two functions
def Total_Order (*Final_order):
    counter=0
    for Food in Final_order: 
        try:                                                # adding the try/except block
            if Food in combos:
                counter += combo_calorie_count(Food)
            else:
                counter += calculate_total_calories(Food)
        except KeyError:
            print(f"Error: '{Food}' is not in any menus.")
    return (counter)




