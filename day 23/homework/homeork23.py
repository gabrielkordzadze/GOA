#1) მომხმარებელს შემოატანინეთ მისი სახელი დიდი ასოებით და შეინახეთ ცვლადში სახელად name და .lower() ფუნქციის მეშვეობით გადააქციეთ ცვლადის
#  მნიშვნელობა  პატარა ასოებად. 


name = input("enter your name In capital letters: ") 
name_lower = name.lower()  


print(" your name In lowercase:", name_lower)


#2) ცვლადში შეინახეთ თქვენი გვარი პატარა ასოებით, შემდეგ .upper() ფუნქციის მეშვეობით გადააქციეთ ცვლადის მნიშვნელობა  დიდ ასოებად.

surname = "kordzadze"
surname = surname.upper()
print("enter your surname in capital letterss: " , surname)

#3) ცვლადში შეინახეთ სტრინგი პატარა ასოებით, შემდეგ .capitalize() ფუნქციის მეშვეობით გადააქციე პირველი ასო დიდ ასოდ.

str = "gabo"
str = str.capitalize()
print("string: " ,str)


#4)ცვლადში შეინახეთ რაიმე სტრინგი,შემდეგ find() ფუნქციის მეშვეობით იპოვეთ რომელ ინდექსზეა კონკრეტული ასო
string = "find the character"
character_index = string.find("c")
print("c character index" ,character_index)


#5)შექმენით სია სტრინგით და თითოეული სტრინგი გადაიყვანეთ დიდ ასოებად for ციკლის მეშვეობით

names = ["gabo", "zura", "andria", "nika", "luka"]

for i in names :
    print(i.upper())



