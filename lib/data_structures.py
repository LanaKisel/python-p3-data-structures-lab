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
    # spicy_foods_list = list()
    # for food in spicy_foods:
    #     spicy_foods_list.append(food["name"])
    # return spicy_foods_list   

    return [food["name"] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    # spicy_foods_list= list()
    # for food in spicy_foods:
    #     if food["heat_level"]>5:
    #         spicy_foods_list.append(food)
    # return spicy_foods_list    
    
    return [food for food in spicy_foods if food["heat_level"] > 5]    
    pass

def print_spicy_foods(spicy_foods):
    
    for food in spicy_foods:
        print(food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + ("🌶" * food["heat_level"]))     
   
   # [print(food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + ("🌶" * food["heat_level"])) for food in spicy_foods]
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + ("🌶" * food["heat_level"]))
    pass

def get_average_heat_level(spicy_foods):
    heat_level = 0
    number_of_foods = 0
    for food in spicy_foods:
        heat_level += food["heat_level"]
        number_of_foods +=1
    average_heat_level = heat_level/number_of_foods
    return average_heat_level 
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods   
    pass
