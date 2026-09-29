#Fuctions for adding calories and camparing totals.


def calculate_total(food_list):
    total=0
    

    for food in food_list:
        total=total+food["calories"]



    return total




def calculate_difference(total,target):
        return total-target