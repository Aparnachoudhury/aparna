# menu={
#     'pizza':80,
#     'pasta':79,
#     'burger':80,
#     'coffee':80
# }

# print("welcome to python restaurant")
# print(" pizza:rs 80 \n pasta:rs 79 \n burger:rs 80 \n coffee:rs 80")

# order_total=0

# item_1=input("enter the name of the item")
# if item_1 in menu:
#     order_total=order_total+menu[item_1]
#     print(f"your item {item_1} has been added ")

# else:
#     print("please order something from the menu")
    
# another_item=input("do you want to order something else? (yes/no):")

# if another_item =="yes":
#     item_2=input("enter the name of the item from menu")
#     if item_2 in menu:
#         order_total=order_total+menu[item_2]
#     else:
#         print("this is not present in our menu..please choose wisely")
 

# print(f"your total bill is: {order_total}")

                   


menu = {
    'pizza': 80,
    'pasta': 79,
    'burger': 80,
    'coffee': 80
}

print("Welcome to Python Restaurant😁😊😉😋")
print("Pizza🍕: Rs 80 \nPasta🍝: Rs 79 \nBurger🍔: Rs 80 \nCoffee🍵: Rs 80")

order_total = 0

item_1 = input("Enter the name of the item🙂: ").strip().lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added.🫠")
else:
    print("Please order something from the menu.😒")

another_item = input("Do you want to order something else? (yes/no): ").strip().lower()

if another_item == "yes":
    item_2 = input("Enter the name of the item from the menu🙂: ").strip().lower()
    if item_2 in menu:
        order_total += menu[item_2]
    else:
        print("This is not present in our menu. Please choose wisely.")
    

print(f"Your total bill is👍🤑: {order_total}\n")
