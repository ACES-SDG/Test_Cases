#3 levels deep nested dictionary
MENU_ = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# level one of the dictionary
# for drink in MENU_:
#     #this should print the drinks and cost
#     print(drink)
#     #this should print the ingredients   
#     for ingredient_list in MENU_[drink]:
#         print(ingredient_list)
#         for item in MENU_[drink][ingredient_list]: 
#             print(item)

# for drink, data in MENU_.items():
#     #this should print the drinks and cost
#     print(drink, data["cost"])
#     #this should print the ingredients   
#     for ingredient in data["ingredients"].items():
#         print(ingredient)