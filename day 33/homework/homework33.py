#You Can't Code Under Pressure #1
def double_integer(i):
    # Double the integer and return it!
    return i * 2



#Friend or Foe?
def friend(x):
    #Code
    result = [] 
    for name in x:  
        if len(name) == 4: 
            result.append(name)  
    return result  

#Beginner - Reduce but Grow
def grow(arr):
    if len(arr) == 1:  # გადამოწმება თუ ერთ-ერთი ელემენტია
        return arr[0]
    return arr[0] * grow(arr[1:])  # გამრავლება პირველი ელემენტის და დანარჩენის



#Calculate average
def find_average(numbers):
    # your code here
    if len(numbers) == 0:  
        return 0
    return sum(numbers) / len(numbers)  


#Grasshopper - #Messi #goals #function
def goals(laLiga, copaDelRey, championsLeague):
     return laLiga + copaDelRey + championsLeague


#Double Char
def double_char(s):
    result = ""  
    for char in s:
        result += char * 2 
    return result


#Remove anchor from URL
def remove_url_anchor(url):
    # TODO: complete
     return url.split('#')[0]




#Sum of Cubes
def sum_cubes(n):
    # your code here
    total = 0  
    for i in range(1, n + 1):
        total += i**3 
    return total 



#1)შექმენით სია, სადაც გექნებათ 5 ელემენტი. წაშალეთ სიის მე-3 ელემენტი და დაამატეთ ახალი მე-0 ინდექსზე. საბოლოოდ დააბრუნეთ ეს სია

def modify_list():
    # 1. შექმნათ სია 5 ელემენტით
    my_list = [1, 2, 3, 4, 5]
    
    # 2. წაშალეთ მე-3 ელემენტი (ინდექსი 2)
    my_list.pop(2)  
    
    # 3. დაამატეთ ახალი ელემენტი მე-0 ინდექსზე
    my_list.insert(0, 10)  
    
    # 4. დავაბრუნოთ სია
    return my_list

print(modify_list()) 





#2)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ ,პირველი რიცხვი აიყვანეთ მეორე რიცხვის ხარისხში და დააბრუნეთ
def power(base, exponent):
    result = 1 
    for _ in range(exponent): 
        result *= base  
    return result  



#3)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია შემდეგ უნდა შეამოწმოთ ამ სიის სიგრძე თუ ლუწია დააბრუნეთ --> List length is even,
#  ხოლო სხვა შემთხვევაში დააბრუნეთ --> List length is odd

def check_list_length(lst):
    if len(lst) % 2 == 0:
        return "List length is even"
    else:
        return "List length is odd"







