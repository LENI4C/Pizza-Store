#TODO:
# Allow customer to specify size, and choice of toppings
#include option of supreme for each size
# disable individual selection if supreme is selected
# display cost of pizza, tax : 6%, then total cost
# confirm project works

hasToppings = True

pizzaType =  [
    {"small pizza" : [10]}, 
    {"medium pizza" : [12]}, 
    {"large pizza" : [15]},
    {"supreme small" : [15, hasToppings ]},
    {"supreme medium" : [20, hasToppings ]},
    {"supreme large" : [27, hasToppings ]}
]

toppings = [
    {"mushrooms" : 1},
    {"pepperoni" : 1},
    {"sausage" : 1},
    {"onions" : 1},
    {"green peppers" : 1},
    {"black olives" : 1},
    {"shrimp" : 1}
]

print("\nALL PIZZAS EXCEPT THE SUPREME PACKAGE COMES PLAIN WITH CHEESE AND TOMATO SAUCE \n\nTHERE'S OPTION FOR TOPPINGS THOUGH\n")

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
        print(f"\nYou have chosen the {pizzaName.upper()},") 

        wantToppings = input("DO YOU WANT TOPPINGS WITH YOUR PIZZA? (Y/N): ").lower()

        # TODO : make the yes option able to add price of each token
        if (wantToppings == "y" or wantToppings == "yes" ):
            i = 0
            print("\nTOPPINGS")
            toppingChoice = []
            toppingName = ["",]
            toppingPrice = ["",]
            top = ""

            if (choiceIndex == 1):
                for topping in toppings:
                    i+=1
                    for choice, attr in topping.items():
                        print(f"{i}) {choice} : ${attr}")
                        toppingName.append(choice)
                        toppingPrice.append(attr)

                while top != "done" : 
                    top = input("\nWHAT TOPPING WOULD YOU LIKE? \nSELECT BY ENTERING THE NUMBER OF THE TOPPING (TO END SELECTION ENTER \"done\"): ").lower()
                    toppingChoice.append(top)

                toppingChoice.pop()
                
                ###################
                chosenToppings = [toppingName[int(tops)] for tops in toppingChoice if 1 <= int(tops) <= len(toppingName) - 1]

                if chosenToppings:
                    if len(chosenToppings) == 1:
                        print("\nYou have chosen " + chosenToppings[0])
                        orderReconfirmation = f"\nYou have opted to have {pizzaName.upper()} with {chosenToppings[0]}"
                        order = f"\n\nYOUR ORDER: \n{pizzaName.upper()} : ${pizzaPrice} \nTOPPINGS: {chosenToppings[0]} (EACH COST ${toppingPrice[1]})  \nTAX: ${tax} (STANDARD 6% VAT)"
                    else:
                        notLastTopping = ", ".join(chosenToppings[:-1])
                        lastTopping = chosenToppings[-1]
                        print(f"\nYou have chosen {notLastTopping}, and {lastTopping}")
                        orderReconfirmation = f"\nYou have opted to have {pizzaName.upper()} with {notLastTopping}, and {lastTopping}"
                        order = f"\n\nYOUR ORDER: \n{pizzaName.upper()} : ${pizzaPrice} \nTOPPINGS: {notLastTopping}, and {lastTopping} (EACH COST ${toppingPrice[1]})  \nTAX: ${tax} (STANDARD 6% VAT)"

                    grossPrice += toppingPrice[1] * int(len(chosenToppings)) 
                    orderCost = f"\nThat'll cost you ${grossPrice}"

                    
                    closingRemark = f"\n\nTHANK YOU FOR SHOPPING WITH US !!!"

                    print(f"{orderReconfirmation}{orderCost}{order}{closingRemark}")
                else:
                    print("No toppings chosen.")
                #####################

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