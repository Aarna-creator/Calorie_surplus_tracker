#Function for keeping the foods entered by the user.


def add_food(food_list,name,calories):
    food={"name":name, "calories":calories}
    food_list.append(food)