#1)შექმენით while loop რომელიც გამოიტანს "hello world!" სანამ არ გაუტოლდება 20'ს
i = 0
while i < 20:
    print("hello world!")
    i += 1

#2)მომხმარებელს შემოატანინეთ სია და for loop ის საშუალებით გამოიტანეთ ყველა ელემენტი
user_input = input("შეიყვანე ელემენტები მძიმით გამოყოფილად: ")
my_list = user_input.split(',')

for item in my_list:
    print(item.strip())


#3)დაწერეთ მსგავსებები და განსხვავებები set, dictionary, tuple ზე 
7
# Set 
my_set = {1, 2, 3, 4}
# - ელემენტები არ მეორდება
# - ინდექსით წვდომა არ აქვს
# - შეგვიძლია ახალი ელემენტის დამატება: my_set.add(5)

# Dictionary 
my_dict = {'name': 'Nino', 'age': 25}
# - თითოეული ელემენტი შედგება "გასაღების" (key) და "მნიშვნელობისგან" (value)
# - key-ები უნიკალურია
# - value-ს წვდომა ხდება key-ის მიხედვით: my_dict['name']

# Tuple 
my_tuple = (10, 20, 30)
# - ინდექსით წვდომა შესაძლებელია: my_tuple[0] → 10
# - ელემენტების შეცვლა არ შეიძლება (immutable)
# - ტუპლები ხშირად გამოიყენება მონაცემების ფიქსირებული ჯგუფებისთვის

# საერთო მახასიათებლები:
# - სამივე ტიპი ინახავს ერთზე მეტ ელემენტს
# - შეგვიძლია for loop-ით გადავლა

# განსხვავებები:
# - set და dict არის "mutable" (შეცვლადი), tuple კი "immutable" (შეუცვლელი)
# - set-ში არ გვაქვს წვდომა ინდექსით, tuple-ში კი გვაქვს
# - dict ინახავს key:value წყვილებს, set და tuple – უბრალოდ ელემენტებს



#4)რას ნიშნავს immutable, mutable
#mutable – ობიექტი, რომელიც შეიძლება შეიცვალოს. მაგ: list, set, dictionary

#immutable – ობიექტი, რომლის ცვლილება შეუძლებელია. მაგ: string, tuple, int

#5)რას ეწოდება კონკატენაცია.

#კონკატენაცია არის ობიექტების (ხშირად სტრიქონების ან სიების) ერთმანეთზე მიწერა/შეერთება.

#6)რას ნიშნავს დეკლარირება.

#დეკლარირება ნიშნავს ცვლადის ან ფუნქციის პირველად შექმნას.

#7)and და or ოპერატორებზე გააკეთეთ 5-5 მაგალითი 

#and ოპერატორი (ორივე პირობა ჭეშმარიტი უნდა იყოს):
print(True and True)   # True
print(True and False)  # False
print(5 > 2 and 3 < 7)  # True
print(10 == 10 and 2 != 3)  # True
print("a" in "apple" and "b" in "banana")  # True

#or ოპერატორი (ერთი მაინც უნდა იყოს ჭეშმარიტი):
print(True or False)   # True
print(False or False)  # False
print(5 > 10 or 3 < 7)  # True
print("a" in "dog" or "d" in "dog")  # True
print(1 == 2 or 2 == 2)  # True

#8)დამატებით გააკეთეთ 5 ცალი 8 kyu და 3 ცალი 7 kyu'ს codewars

#8kyu

#How good are you really?
def better_than_average(class_points, your_points):
    # Your code here
    average = sum(class_points) / len(class_points)
    return your_points > average


#Surface Area and Volume of a Box
def get_size(w,h,d):
    #your code here
    area = 2 * (w * h + h * d + d * w)
    volume = w * h * d
    return [area, volume]


#Beginner - Lost Without a Map
def maps(a):
    result = []
    for i in a:
        result.append(i * 2)
    return result



#Take the Derivative
def derive(coefficient, exponent): 
    # your code here
    result = coefficient * exponent
    
    exponent -= 1
    
    return str(result) + "x^" + str(exponent)


#Return the day
def whatday(num):
  # Put your code here
    if num == 1:
        return "Sunday"
    elif num == 2:
        return "Monday"
    elif num == 3:
        return "Tuesday"
    elif num == 4:
        return "Wednesday"
    elif num == 5:
        return "Thursday"
    elif num == 6:
        return "Friday"
    elif num == 7:
        return "Saturday"
    else:
        return "Wrong, please enter a number between 1 and 7"
    



#7 kyu

#V A P O R C O D E
def vaporcode(s):
    #your code here
    result = []  
    for i in s:
        if i != " ":  
            result.append(i.upper()) 
    return '  '.join(result)



#Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    #your code here
    numbers.sort()
    return numbers[0] + numbers[1]


#Friend or Foe?
def friend(x):
    #Code
    result = []  
    for name in x: 
        if len(name) == 4:
            result.append(name)  
    return result  