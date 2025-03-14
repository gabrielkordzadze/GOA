#1)გადახედეთ ამ რესურსებს:
#https://www.w3schools.com/python/python_tuples.asp
#https://www.w3schools.com/python/python_tuples_access.asp
#https://www.w3schools.com/python/python_tuples_update.asp
#https://www.w3schools.com/python/python_tuples_unpack.asp
#https://www.w3schools.com/python/python_tuples_loop.asp

#2) შემენით tuple, რომელშიც შეინახავთ საყიდლების სიას და მოახდინეთ მათი unpacking (დაშლა),რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.
# საყიდლების სია
shopping_list = ("bread", "milk", "egg", "apple")

# Unpacking
item1, item2, item3, item4 = shopping_list

# ცვლადების ბეჭდვა
print(item1)  # bread
print(item2)  # milk
print(item3)  # egg
print(item4)  # apple

#3) შექმენით tuple და შეინახეთ Fast food პროდუქტები. შემდეგ შეცვალეთ ეს tuple და მათში ჩაამატეთ ჯანსაღი საკვები პროდუქტები.
fast_food = ("ბურგერი", "ფრი", "პიცა")
fast_food = list(fast_food)
fast_food[0] = "apple"
fast_food[1] = "fish"
fast_food[2] = "salad"
print(tuple(fast_food))

#4) კომენტარის სახით ახსენით, თუ რა ფუნქციას ასრულებს Asterisk და როგორ აღინიშნება ის.
#Asterisk (*) გამოიყენება unpacking-ის დროს, როცა გვინდა, რომ რამდენიმე ელემენტი შევინახოთ ერთ ცვლადში.

#5) მოცემულია შემდეგნაირი tuple:

months = ("January", "February", "March", "April", "May")
#(first, second, third, fourth*)= months

#რას გამოიტანს მოცემული კოდი?
print(first)
print(second)
print(third)
print(fourth)

#Python-ში * (asterisk) უნდა იყოს ცვლადის წინ, მაგრამ fourth* არასწორი სინტაქსია. სწორი ფორმაა *fourth.