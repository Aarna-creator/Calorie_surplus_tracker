#Start the calorie tracker.
  
from input_helpers import get_number
from food_data import add_food
from calculator import calculate_total,calculate_difference
from results import show_results

def main():
    print("Calorie Surplus Tracker")
    print("This program /campares food calories with a target you enter.")
    print("It does not recommend a calorie target, but it will tell you if you are over or under your target.")


    target=get_number("Enter your daily calorie target:")
    while target<=0:
 
        print("Please enter a number greater tan zero.")
        target=get_number("Enter your daily calorie target ")


    foods=[]

    while True:
        name=input("Enter a food name,or type done to finish:")
        name=name.strip()

        if name.lower()=="done":
            break
 
        if name=="" :
            print("Please enter a food name:")
        
        else:
            calories=get_number("Enter its calories:")
            add_food(foods,name,calories)

    
    total=calculate_total(foods)
    difference =calculate_difference(total,target)
    show_results(foods,total,target,difference)



if __name__ == "__main__":


    main()