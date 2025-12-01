# def vendingMachine(products, balance):
#     for i in products:
#         print(i)

#     print()
#     print(f'your balance is {balance}$')
#     print()
#     user_input = int(input('Enter a product number: '))
#     product = products[user_input][:-3]

#     print(f'you got {product}')



# vendingMachine(['2$ - Snickers (0)', '5$ - Oreo (1)', '2$ - KitKat (2)', '2$ - Bounty (3)', '3$ - Mars (4)', 
#                 '4$ - Twix (5)', '6$ - Haribo (6)'], 10) 



def vendingMachine(products, balance):
    print("Available products:")
    for i, item in enumerate(products):
        print(f"{i}: {item}")

    print(f"\nYour balance is ${balance}\n")

    user_input = int(input("Enter a product number: "))
    
    # პროდუქტის ფასი და სახელი
    price = int(products[user_input].split('$')[0])
    product_name = products[user_input].split('-')[1].strip().split('(')[0].strip()

    if balance >= price:
        balance -= price
        print(f"You got {product_name}!")
        print(f"Remaining balance: ${balance}")
    else:
        print(f"Not enough money for {product_name}. You need ${price}, but have ${balance}.")

# გამოცდა
vendingMachine(
    ['2$ - Snickers (0)', '5$ - Oreo (1)', '2$ - KitKat (2)', '2$ - Bounty (3)', 
     '3$ - Mars (4)', '4$ - Twix (5)', '6$ - Haribo (6)'], 10
)
