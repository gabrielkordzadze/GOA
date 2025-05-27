#1)შექმენით დიქშენერი რომელშიც შეინახავთ თქვენი საყვარელი მანქანის აღწერას ბრენდის სახელს, მოდელსა და გამოშვების წელს შემდეგ დიქშენერიდან 
#ამოიტანეთ გასაღებები და მნიშვნელობები წყვილად შემდეგ კი ცალ-ცალკე 

car = {
    "ბრენდი":"BMW",
    "მოდელი":"E30",
    "გამოშვების წელი":"1982"

 }


# გასაღებები და მნიშვნელობები წყვილად
for key, value in car.items():
    print(f"{key}: {value}")

# გასაღებები ცალ-ცალკე
print("Keys:", car.keys())

# მნიშვნელობები ცალ-ცალკე
print("Values:", car.values())


#2)შექმენით 2 სეტი და ჯერ შეაერთეთ ერთმანეს შემდეგ გამოიტანეთ გნსხვავებები და მსგავსებები მათ შორის
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# გაერთიანება
union_set = set1.union(set2)
print("Union:", union_set)

# განსხვავება (მხოლოდ set1-ში არსებული ელემენტები)
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# მსგავსება (ერთნაირი ელემენტები)
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)
 
#3)შექმენით დიქშენერი რომლის მნიშვნელობებსაც გადაატარებთ forloop'ს და გამოიტანეთ ისინი ისინი
person = {
    "სახელი": "გაბრიელი",
    "ასაკი": 13,
    "ქალაქი": "ქარელი"
}

for value in person.values():
    print(value)

#4)ახსენით დიქშენერი და სეტები კომენტარის სახით

# Dictionary (ლექსიკონი) – მონაცემთა სტრუქტურაა, რომელიც ინახავს key-value წყვილებს.
# თითოეულ key-ს აქვს შესაბამისი value, და key-ები უნიკალურია.

# Set (მრავლობა) – უნიკალური ელემენტების არადამთხვევადი კოლექციაა, სადაც ელემენტები არ მეორდება.


#5)შექმენით dictionary და ცარიელი სია, შემდეგ for ციკლის მეშვოებით გადაუარეთ dictionary-ს და ჩაამატეთ მისი key და value-ბი სიაში
data = {
    "a": 10,
    "b": 20,
    "c": 30
}

list_storage = []

for key, value in data.items():
    list_storage.append((key, value))

print("List with dictionary items:", list_storage)

#6)შექმენით dictionary სადაც შეინახავთ მინიმუმ 3 key / value წყვილს, შემდეგ მომხმარებელს შეეკითხეთ შემოიტანოს key და value,
#  შემდეგ შეამოწმეთ თუ შექმნილ dict-ში არ გვაქვს მსგავსი key, მაშინ ჩაამატეთ ეს წყვილი, სხვა შემთხვევაში გამოიტანეთ "Key already exists!"

info = {
    "username": "gabo",
    "password": "1234",
    "email": "admin@example.com"
}

user_key = input("Enter a key: ")
user_value = input("Enter a value: ")

if user_key not in info:
    info[user_key] = user_value
    print("New key-value pair added!")
else:
    print("Key already exists!")

print("Updated dictionary:", info)

