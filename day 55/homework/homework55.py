#1) შექმენით dictionary სადაც შეინახავთ მინიმუმ 3 key'ს და ასევე შექმენით 2 ცარიელი სია for loop'ის დახმარებით პირველ სიაში დაამატეთ key ხოლო
#მეორე სიაში კი value ბოლოს კი გამოიტანეთ ერთად. 
data = {
    "name": "gabrieli",
    "age": 13,
    "city": "khareli"
}

keys_list = []
values_list = []

for key, value in data.items():
    keys_list.append(key)
    values_list.append(value)

# Keys და Values ერთად
print("Keys:", keys_list)
print("Values:", values_list)



#2) მოცემული გაქვთ რაიმე result ცვლადი რომელშიც შეყვანილია სია [10,43,12,11,94,10,55,7,11] თქვენი დავალებაა გააქროთ ყველა დუბლიკატი ლისტიდან
#  „თანმიმდევრობას მნიშვნელობა არაქვს“.

result = [10, 43, 12, 11, 94, 10, 55, 7, 11]

unique_list = []
for num in result:
    if num not in unique_list:
        unique_list.append(num)

print("Unique list:", unique_list)


#3) დღევანდელ ახსნილ მეთოდებზე გააკეთეთ მაგალითები თითო მეთოდზე 5 მაგალითი მაინც.

# .update() – ამატებს ერთი set-ს და უთავსებს მეორის ელემენტებს
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set1.update(set2)
print(set1)

set1.update([7, 8, 9])
print(set1)

set1.update((10, 11))
print(set1)

set1.update("abc")
print(set1)

set1.update({12, 13, 14})
print(set1)

# .union() – აერთიანებს ორ set-ს და აბრუნებს ახალ set-ს
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.union(set2))

set3 = {7, 8, 9}
print(set1.union(set2, set3))

print(set1.union([10, 11, 12]))

print(set1.union("abc"))

print(set1.union(set()))

# .difference() – აბრუნებს set-ს სხვაობით
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set1.difference(set2))

print(set2.difference(set1))

set3 = {2, 3}
print(set1.difference(set2, set3))

set4 = {10, 11}
print(set1.difference(set4))

print(set1 - set2)

# .symmetric_difference() – აბრუნებს set-ს ორმხრივი სხვაობით
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set1.symmetric_difference(set2))

set3 = {8, 9}
print(set1.symmetric_difference(set3))

set4 = {1, 2, 3, 4, 5}
print(set1.symmetric_difference(set4))

print(set1 ^ set2)

print(set1.symmetric_difference(set()))

# .intersection() – პოულობს საერთო ელემენტებს ორ set-ში
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set1.intersection(set2))

set3 = {4, 5, 6, 7, 8}
print(set1.intersection(set2, set3))

set4 = {10, 11}
print(set1.intersection(set4))

set5 = {2, 3, 4}
print(set1 & set5)

print(set1.intersection(set1))

# .remove() – წაშლის ელემენტს set-დან (თუ არ არსებობს, Error)
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)

set1.remove(5)
print(set1)

set1.remove(1)
print(set1)

set1.remove(2)
print(set1)

# set1.remove(10)  # Error

# .discard() – წაშლის ელემენტს set-დან (Error-ს არ აგდებს)
set1 = {1, 2, 3, 4, 5}
set1.discard(3)
print(set1)

set1.discard(10)  # არაფერს არ გააკეთებს

set1.discard(5)
print(set1)

set1.discard(1)
print(set1)

set1.discard(2)
print(set1)

# .clear() – set-ის ყველა ელემენტის წაშლა
set1 = {1, 2, 3, 4, 5}
set1.clear()
print(set1)

set2 = {"apple", "banana"}
set2.clear()
print(set2)

set3 = {True, False}
set3.clear()
print(set3)

set4 = {None}
set4.clear()
print(set4)

set5 = set()
set5.clear()
print(set5)

# del – მთლიანად set-ის წაშლა
set1 = {1, 2, 3, 4, 5}
del set1
# print(set1)  # Error

set2 = {"apple", "banana"}
del set2
# print(set2)  # Error

set3 = {True, False}
del set3
# print(set3)  # Error

set4 = {None}
del set4
# print(set4)  # Error

set5 = set()
del set5
# print(set5)  # Error



#4) შექმენით ცარიელი dictionary შემდეგ მომხმარებელს შემოატანინეთ ჯერ key  შემდეგ კი value ამის შემდეგ თხოვეთ შეცვალოს ძველი value
#   და შემოატანინეთ ახალი მნიშვნელობა შემდეგ კი გამოიტანეთ საბოლოო dictionary.

user_dict = {}

user_key = input("Enter a key: ")
user_value = input("Enter a value: ")

user_dict[user_key] = user_value

# ძველი მნიშვნელობის შეცვლა
new_value = input(f"Enter a new value for '{user_key}': ")
user_dict[user_key] = new_value

print("Final dictionary:", user_dict)

#5) შექმენით სეტის მსგავსი ფუნქცია რომელიც მიიღებს ლისტს და ლისტიდან წაშლის დუბლიკატებს „ფუნქციაში არ გამოიყენოთ სეტი“

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list