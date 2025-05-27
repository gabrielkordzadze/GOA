#Sum of a sequence
def sequence_sum(begin_number, end_number, step):
    #your code here
    if begin_number > end_number:
        return 0
    
    total_sum = 0
    
    for i in range(begin_number, end_number + 1, step):
        total_sum += i
        
    return total_sum
    

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



#Sum Mixed Array
def sum_mix(arr):
    #your code here
    total = 0
    for x in arr:
        total += int(x)  # ყველა ელემენტს ვაქცევთ მთელ რიცხვად და ვუმატებთ ჯამს
    return total


#Array plus array
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)


#Reversed Words
def reverse_words(s):
    return " ".join(s.split()[::-1])


#Sum The Strings
def sum_str(a, b):
    # happy coding !
    return str(int(a or 0) + int(b or 0))