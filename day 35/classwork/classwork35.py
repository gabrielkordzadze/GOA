#Find the capitals
def capitals(word):
    #your code here
    indices = []  # შევქმნათ ცარიელი სია, სადაც ჩავდებთ ინდექსებს
    for i in range(len(word)):  # ვადევნებთ თვალს სტრიქონის თითოეულ ასოს
        if word[i].isupper():  # თუ ასო არის დიდი (uppercase)
            indices.append(i)  # მისი ინდექსი დამატებული იქნება სიაში
    return indices  # დავაბრუნოთ ინდექსები



#Maximum Multiple
def max_multiple(divisor, bound):

    #your code here
    for i in range(bound, 0, -1):
        # თუ i მთლიანად იყოფა divisor-ით, მაშინ ის არის ჩვენი შედეგი
        if i % divisor == 0:
            return i  # ვბრუნდებით პირველივე რიცხვზე, რომელიც შეესაბამება მოთხოვნებს
        

#Summing a number's digits
def sum_digits(number):
    total = 0
    if number < 0:  # თუ რიცხვი ნეგატიურია
        number = -number  # ნეგატიური რიცხვი დადებითად გადავაქციოთ
    else:
        number = number  # სხვა შემთხვევაში, რიცხვი უკვე დადებითია

    # ციფრების დამატება ჯამში
    while number > 0:
        total += number % 10  # ბოლო ციფრის დამატება
        number //= 10  # რიცხვის ციფრის ამოღება

    return total


#Don't give me five!
def dont_give_me_five(start, end):
    count = 0
    for num in range(start, end + 1):
        check_num = num
        if check_num <0:
            check_num = - check_num
        fives = 0
        while check_num > 0:
            if check_num % 10 == 5:
                fives = 1
            check_num //= 10
        if fives == 0:
            count += 1
    return count


#Fizz Buzz
def fizzbuzz(n):
    result = []  
    for i in range(1, n + 1):  
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")  
        elif i % 3 == 0: 
            result.append("Fizz") 
        elif i % 5 == 0:  
            result.append("Buzz")  
        else:
            result.append(i)
    return result  


#Invert values
def invert(lst):
    result = []  
    for num in lst:  
        result.append(-num) 
    return result

#Sum without highest and lowest number
def sum_array(arr):
    if arr == None or len(arr) <= 2:
        return 0
    return sum(arr) - min(arr) - max(arr)

    




