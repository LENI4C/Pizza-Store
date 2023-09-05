#TODO:
# Allow customer to specify size, and choice of toppings
#include option of supreme for each size
# diable individual selection if supreme is selected
# display cost of pizza, tax : 6%, then total cost
# confirm project works

hasToppings = True

toppingSmall = 1
toppingMedium = 1.50
toppingLarge = 2.25

toppings = [
    {"mushrooms" : 1},
    {"pepperoni" : 1},
    {"sausage" : 1},
    {"onions" : 1},
    {"green peppers" : 1},
    {"black olives" : 1},
    {"shrimp" : 1}
]

pizzaType =  [
    {"small pizza" : [10]}, 
    {"medium pizza" : [12]}, 
    {"large pizza" : [15]},

    {"supreme small" : [15, hasToppings ]},
    {"supreme medium" : [20, hasToppings ]},
    {"supreme large" : [27, hasToppings ]}
]

print("\nALL PIZZAS EXCEPT THE SUPREME PACKAGE COMES PLAIN WITH CHEESE AND TOMATO SAUCE \n\nTHERE ARE CHOICES FOR OPTIONAL TOPPINGS THOUGH")


def userAlgorithm():
    i = 0
    # interesting thingy going on here, i set the first item in the list to be an empty string so that when user selects 1 it'll not give them medium pizza instead of the ideal small pizza which it should've given them
    options = ["",]
    for pizza in pizzaType:
        i+=1
        for choice, attr in pizza.items():
            print(f"{i}) {choice} : {attr[0]}$")
            options.append(choice)

    listChoiceIndex = int(input("WHAT KIND OF PIZZA WOULD YOU LIKE : \nSELECT BY ENTERING THE INDEX OF THE PIZZA: "))
    if (options[listChoiceIndex] <= options[3]):       
        print(f"you have chosen {options[listChoiceIndex]}, and you are eligible to get toppings") 

        print("\nTOPPINGS")
        for topping in toppings:
            for choice, attr in topping.items():
                print(f"{choice} : {attr}$")



userAlgorithm()
# print("\nPIZZA\n")

# pizzaChoice = 

# if (pizzaChoice == ) :


