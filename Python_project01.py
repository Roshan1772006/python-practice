# define the menu if restaurant
menu ={
    'Pizza':40,
    'Pasta':50,
    'Burger':70,
    'Salad':60,
    'Coffee':80,
}

print("Welcome to Python Restaurant")
print('Pizza:40\nPasta:50\nBurger:70\nSalad:60\nCoffee:80')

order_total=0
item_1= input("enter the name of item you want to order = ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f'Your item {item_1} has been added to your order')
else:
    print(f"order item {item_1} is not avaialable yet!")
    
another_order = input ("Do you want to add anither item? (Yes/No)")

if another_order == "Yes" or another_order=="yes":
    item_2 = input("Enter the second item  = ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f'Your item {item_2} has been added to your order')
        print(order_total)
    else:
        print(f"order item {item_2} is not avaialable yet!")
else:
    print(order_total) 
print("THANK YOU VISTING YOUR PYTHON RESTAURANT")