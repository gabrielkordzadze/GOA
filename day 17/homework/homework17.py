#1)შექმენით სია შემდგარი 5 ელემენტისგან და გამოიტანეთ ამ სიის თითოეული ელემენტი ინდექსებით
list1 = ["a", "b", "c", "d", "e"]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])


#)შექმენით სია შემდგარი 10 ელემენტისგან და გამოიტანეთ თითოეული ელემენტი for ციკლით / range() ფუნქციითაც და პირდაპირ ცვლადის გადაცემითაც


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# გამოყვანა for ციკლით და range() ფუნქციით

for i in my_list:
    print(my_list[i])

# გამოყვანა პირდაპირი ცვლადის გადაცემით
for item in my_list:
    print(item)

#3)შექმენით სია შემდგარი რიცხვებისგან, გადაუარეთ for ციკლით და გამოიტანეთ მხოლოდ ის რიცხვები რომელიც მეტია 10ზე

numbers = [5, 12, 7, 18, 9, 15, 2, 25, 8, 30]



for number in numbers:
    if number > 10:
        print(number)


#4)შექმენით სია შემდგარი 7 განსხვავებული ემენეტისგან და for ციკლის მეშვეობით შეამოწმეთ თითოეული ემენეტის მონაცემთა ტიპი
# სიის შექმნა
my_list = [42, "text", 3.14, True, False, 1, 2, 3 ]

# for ციკლით მონაცემთა ტიპების გამოყვანა
print("მონაცემთა ტიპები:")
for element in my_list:
    print(type(element))


