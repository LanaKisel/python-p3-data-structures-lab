# spicy_foods = [
#     {
#         "name": "Green Curry",
#         "cuisine": "Thai",
#         "heat_level": 9,
#     },
#     {
#         "name": "Buffalo Wings",
#         "cuisine": "American",
#         "heat_level": 3,
#     },
#     {
#         "name": "Mapo Tofu",
#         "cuisine": "Sichuan",
#         "heat_level": 6,
#     },
# ]

# def get_names(spicy_foods):
#     # spicy_foods_list = list()
#     # for food in spicy_foods:
#     #     spicy_foods_list.append(food["name"])
#     # return spicy_foods_list   

#     return [food["name"] for food in spicy_foods]
#     pass

# def get_spiciest_foods(spicy_foods):
#     # spicy_foods_list= list()
#     # for food in spicy_foods:
#     #     if food["heat_level"]>5:
#     #         spicy_foods_list.append(food)
#     # return spicy_foods_list    
    
#     return [food for food in spicy_foods if food["heat_level"] > 5]    
#     pass

# def print_spicy_foods(spicy_foods):
    
#     for food in spicy_foods:
#         print(food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + ("🌶" * food["heat_level"]))     
   
#    # [print(food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + ("🌶" * food["heat_level"])) for food in spicy_foods]
#     pass

# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     for food in spicy_foods:
#         if food["cuisine"] == cuisine:
#             return food
#     pass

# def print_spiciest_foods(spicy_foods):
#     for food in spicy_foods:
#         if food["heat_level"] > 5:
#             print(food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + ("🌶" * food["heat_level"]))
#     pass

# def get_average_heat_level(spicy_foods):
#     heat_level = 0
#     number_of_foods = 0
#     for food in spicy_foods:
#         heat_level += food["heat_level"]
#         number_of_foods +=1
#     average_heat_level = heat_level/number_of_foods
#     return average_heat_level 
#     pass

# def create_spicy_food(spicy_foods, spicy_food):
#     spicy_foods.append(spicy_food)
#     return spicy_foods   
#     pass

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

def get_names(foods):
  return [food['name'] for food in foods]

def get_spiciest_foods(foods):
  return [food for food in foods if food['heat_level'] >5]

def print_spicy_foods(foods):
  for food in foods:
    print(food['name'] + " (" + food['cuisine'] + ") | Heat Level: " + ('🌶' *food['heat_level']))

def get_spicy_food_by_cuisine(foods, cuis):
    for food in foods:
        if food['cuisine'] == cuis:
            return food

def print_spiciest_foods(foods):
    print_spicy_foods(get_spiciest_foods(foods))

import statistics
def get_average_heat_level(foods):
  heat_l_list = list()
  for food in foods:
    heat_l_list.append(food['heat_level'])
  return statistics.mean(heat_l_list)
 

def create_spicy_food(foods, new_food):
  foods.append(new_food)
  return foods