#coffee machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}
profit=0
def report():
    global resources,profit
    print (resources)
    print(f"The profit is: ${profit}")
cont=True
while cont:

    price=True
    y=True

    coffee=input("What coffee do you want to command? Espresso,latte or cappuccino?\n").lower()
    if coffee=='report':
        report()
        break
    money=float(input("Introduce here you money please\n$"))
    cost_coffee=MENU[coffee]["cost"]


    while price:
        if money<cost_coffee:
            print("You need to add more bc cost of the coffee is higher.")
            money=float(input("Introduce here you money please\n$"))
        else:
            price=False
            print(f"Here is your rest. ${(money-cost_coffee)}")
            profit+=money-cost_coffee


    list_of_ing_nec_value=[]
    for nec_ing_value in MENU[coffee]["ingredients"]:
        list_of_ing_nec_value.append(MENU[coffee]["ingredients"][nec_ing_value])


    resources_list=[] #value
    res_prd=[] #actual res
    for i in resources:
        resources_list.append(resources[i])
        res_prd.append(i)
    #print (resources_list)
    #print(res_prd)
    

    while y:
        for i in range(len(resources_list)) and range(len(list_of_ing_nec_value)) and range(len(res_prd)):
                resources_list[i]-=list_of_ing_nec_value[i]
                if resources_list[i]<0:
                    print(f"We can't to do your {coffee} bc we dont't have enough {res_prd[i]}. Here is your refund. {money}")
                    y=False
                    cont=False
        break
    if y==True:
        print(f"Here is you {coffee}. Enjoy it!")
        for i in range(len(res_prd)) and range(len(resources_list)):
            resources[res_prd[i]]=resources_list[i]
    #print(resources)
        ans=input("Do you want another coffee? Type here 'y' or 'n'\n")
        if ans=='n':
            cont=False
        elif ans=='report':
            report()
