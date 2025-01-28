#Menu of restaurant,
MENU = {
     'PIZZA' : 100,
     'BURGER': 50,
     'PASTA' : 80,
     'CHOWMIEN': 60,
     'SANDWICH': 80,
     'MOMOS': 60,
     'SPRINGROLL': 60,
     'FRIES': 70
}
#Greet
print("******WELCOME TO THE PYTHON RESTAURANT******")
print(" PIZZA: RS100\n BURGER: RS50\n PASTA: RS80\n CHOWMIEN: RS60\n SANDWICH: RS60\n MOMOS:RS60\n SPRINGROLL:RS60\n FRIES:RS70")

total_amount = 0
items = 0

while items<=10:
    USER_ITEM = input("Enter your item: ")
    if USER_ITEM in MENU:
        total_amount += MENU[USER_ITEM]
        print(f"Your item {USER_ITEM} has been added to your order")
    elif USER_ITEM == "EXIT":
        print(f"The total amount of your order is RS{total_amount}\nThankyou for your order.")
        break
    else:
        print("This item is not available, choose another item!!")







