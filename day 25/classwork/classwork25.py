#1)შექმენით სია რომელშიც იქნება 5 სახელი შემდეგ, ამოიღეთ სიიდან პირველი და ბოლო ელემენტი
# შექმნათ სია
names = ["კახა", "ნატალია", "გიორგი", "მარიამი", "თამარი"]


names.pop(0)  
names.pop()  

print(names)  

#2)კომეტარებით ახსენით რას აკეთებს თითოეული ფუნქცია:

#.insert()
#.append()
#.pop()
#.len()

#insert(index, value): დაამატებს ელემენტს მოცემულ ინდექსზე.
#.append(value): დაამატებს ელემენტს სიის ბოლოს.
#.pop(index): ამოიღებს ელემენტს მოცემულ ინდექსზე.
#len(): აბრუნებს სიის ელემენტების რაოდენობას.




#3) შექმენით სია რომელიც შედგება 5 სახელისგან შემდეგ insert მეთოდით დაამატეთ ახალი სახელი სიის მეორე ინდექსზე

names = ["გივი", "მარიამი", "მაკა", "ნინო", "ირაკლი"]

names.insert(2, "დიმიტრი")

print(names)  