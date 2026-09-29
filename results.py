#Show the food list and daily calorie summary.


def show_results(food_list, total, target, difference):
    print("\nFoods entered:")

    if len(food_list) == 0:
        print("No foods were entered.")
    else:
        for food in food_list:
            print(food["name"] + ": " + str(food["calories"]) + " calories")

    print("\nTotal calories: " + str(total))
    print("Daily target: " + str(target))

    if difference > 0:
        print("You are " + str(difference) + " calories above your target.")
    elif difference < 0:
        print("You are " + str(abs(difference)) + " calories below your target.")
    else:
        print("You are exactly at your target.")

    print("\nThis is only a simple tracking calculation, not nutrition advice.")

