#List Filtering
def filter_list(l):
    result = []
    for x in l:
        if type(x) == int:  # თუ x არის მთელი რიცხვი
            result.append(x)  # დავამატოთ result სიაში
    return result  # დავაბრუნოთ გაფილტრული სია
    


#Jaden Casing Strings
def to_jaden_case(string):
    # ...
    exceptions = ["aren't", "isn't", "can't", "won't", "don't", "didn't", "hasn't", "haven't", "wasn't", "weren't"]
    
    result = ""
    word = ""
    
    for char in string + " ":  # ვამატებთ სივრცეს, რათა ბოლო სიტყვაც დამუშავდეს
        if char == " ":
            if word.lower() in exceptions:
                result += word.capitalize() + " "
            else:
                result += word.capitalize() + " "
            word = ""
        else:
            word += char
    
    return result.strip()



#Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    #your code here
    numbers.sort()
    return numbers[0] + numbers[1]



#Is this a triangle?
def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a


#Two to One
def longest(a1, a2):
    # your code
    return ''.join(sorted(set(a1 + a2)))