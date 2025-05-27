#1)შექმენით ცარიელი სია და for ციკლის მეშვეობით ჩაამატეთ ყველა ლუწი რიცხვი 0დან 200მდე, ბოლოს დაბეჭდეთ სია.
numbers = []
for i in range(201):
    if i % 2 == 0:
        numbers.append(i)
print(numbers)



#2)შექმენით ცარიელი სია და for ციკლის მეშვოებით მომხმარებელს შეეკითხეთ მისი top 5 საყვარელი სახელი (ანუ ხუთჯერ input).
favorite_name = []
for i in range(5):
    name = input("enter your favorite name")
    favorite_name.append(name)
print(favorite_name)




#3)შექმენით სია 10 ელემენტით და გამოიტანეთ მხოლოდ კენტ ინდექსზე მდგომი ელემენტები.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len (my_list)):
    if i % 2 != 0:
        print(my_list[i])

#4)შექმენით ცვლადი რომელშიც შენახული იქნება სტრინგი შემდეგ კი გაიგეთ ამ სტრინგის სიმბოლოების რაოდენობა.
my_string = "string"
print(f"symbols: {len(my_string)}")

#5)შექმენით სია შემდგარი 5 ელემენტისგან, მომხმარებელს შემოატანინეთ რიცხვი და სიიდან ამოაგდეთ შემოტანილ რიცხვის ინდექსზე მდგომი ელემენტი.
my_list = [10, 20, 30, 40, 50]
index = int(input("შეიყვანეთ ამოსაღები ელემენტის ინდექსი (0-დან 4-მდე): "))
if 0 <= index < len(my_list):
    my_list.pop(index)
else:
    print("არასწორი ინდექსი!")
print(my_list)


#6)შექმენით სია და დაბეჭდეთ ამ სიის სიგრძე.
my_list = [5, 10, 15, 20, 25]
print(f"სიის სიგრძე არის: {len(my_list)}")

