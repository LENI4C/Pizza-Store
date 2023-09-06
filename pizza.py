#TODO:
# Allow customer to specify size, and choice of toppings
#include option of supreme for each size
# disable individual selection if supreme is selected
# display cost of pizza, tax : 6%, then total cost
# confirm project works

hasToppings = True

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

print("\nALL PIZZAS EXCEPT THE SUPREME PACKAGE COMES PLAIN WITH CHEESE AND TOMATO SAUCE \n\nTHERE'S OPTION FOR TOPPINGS THOUGH")

def pizzaAlgorithm():
    i = 0
    # interesting thingy going on here, I set the first item in the list to be an empty string so that when user selects 1 it'll not give them medium pizza instead of the ideal small pizza which it should've given them
    options = ["",]
    optionPrices = ["",]
    for pizza in pizzaType:
        i+=1
        for choice, attr in pizza.items():
            print(f"{i}) {choice} : ${attr[0]}")
            options.append(choice)
            optionPrices.append(attr[0])

    choiceIndex = int(input("\nWHAT KIND OF PIZZA WOULD YOU LIKE? \nSELECT BY ENTERING THE NUMBER OF THE PIZZA: "))
    pizzaName = options[choiceIndex]
    pizzaPrice = optionPrices[choiceIndex]
    tax = 0.06 * pizzaPrice
    grossPrice = tax + pizzaPrice
    orderReconfirmation = f""
    orderCost = f""
    order = f""
    closingRemark = f""

    if (choiceIndex > 0 and choiceIndex < 4):       
        print(f"\nYou have chosen the {pizzaName.upper()}, and you are eligible to get toppings") 

        wantToppings = input("\nDO YOU WANT TOPPINGS WITH YOUR PIZZA? (Y/N): ").lower()

        if (wantToppings == "y" or wantToppings == "yes" ):
            print("\nTOPPINGS")
            if (choiceIndex == 1):
                for topping in toppings:
                    for choice, attr in topping.items():
                        print(f"{choice} : ${attr}")
            elif (choiceIndex == 2):
                for topping in toppings:
                    for choice, attr in topping.items():
                        print(f"{choice} : ${attr * 1.5}")
            else:
                for topping in toppings:
                    for choice, attr in topping.items():
                        print(f"{choice} : ${attr * 2.25}")


        elif (wantToppings == "n" or wantToppings == "no" ):

            orderReconfirmation = f"\nYou have opted to have your {pizzaName.upper()} without any toppings"

            orderCost = f"\nThat'll cost you ${grossPrice}"

            order = f"\n\nYOUR ORDER: \n{pizzaName.upper()} : ${pizzaPrice} \nTAX: ${tax} (STANDARD 6% VAT)"
            
            closingRemark = f"\n\nTHANK YOU FOR SHOPPING WITH US !!!"

            print(f"{orderReconfirmation}{orderCost}{order}{closingRemark}")

            


pizzaAlgorithm()