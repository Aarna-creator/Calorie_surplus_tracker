#Functions for asking the user to enter number.



def get_number(question):
    while True:
         answer=input(question)


         if answer.isdigit():
            return int(answer)
         else:
            print("Please enter a whole number,such as 230.")
            