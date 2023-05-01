spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # Without List Comprehensions
    # names = []
    # for food in spicy_foods:
    #     names.append(food["name"])
    # return names

    # With List Comprehensions
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(food["name"] + " (" + food["cuisine"] +  ") " + "| Heat Level: " + ("🌶" * food["heat_level"]))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    # Long solution
    # for food in spicy_foods:
    #     if food["heat_level"] > 5:
    #         print(food["name"] + " (" + food["cuisine"] +  ") " + "| Heat Level: " + ("🌶" * food["heat_level"]))

    # Shorter solution - using preexisting functions!
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    heat = []
    for food in spicy_foods:
        heat.append(food["heat_level"])
    return (heat[0] + heat[1] + heat[2]) / 3     

def create_spicy_food(spicy_foods, spicy_food):
    # pass
    spicy_food = {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
    spicy_foods.append(spicy_food)
    return spicy_foods