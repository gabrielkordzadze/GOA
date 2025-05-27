#Jaden Casing Strings
def to_jaden_case(string):
    # ...
    exceptions = ["aren't", "isn't", "can't", "won't", "don't", "didn't", "hasn't", "haven't", "wasn't", "weren't"]
    
    result = ""
    word = ""
    
    for i in string + " ":  # ვამატებთ სივრცეს, რათა ბოლო სიტყვაც დამუშავდეს
        if i == " ":
            if word.lower() in exceptions:
                result += word.capitalize() + " "
            else:
                result += word.capitalize() + " "
            word = ""
        else:
            word += i
    
    return result.strip()


#Sum of a sequence
def sequence_sum(begin_number, end_number, step):
    #your code here
    if begin_number > end_number:
        return 0
    
    total_sum = 0
    current = begin_number
    
    while current <= end_number:
        total_sum += current
        current += step
        
    return total_sum


#Regex count lowercase letters
def lowercase_count(strng):
    # Your code here
    count = 0
    for i in strng:
        if i.islower():
            count += 1
    return count


#How good are you really?
def better_than_average(class_points, your_points):
    # Your code here
    average = sum(class_points) / len(class_points)
    return your_points > average


#Beginner - Reduce but Grow
def grow(arr):
    result = 1
    for num in arr:
        result = result * num 
    return result


#Sentence Smash
def smash(words):
    return " ".join(words)


#3)შექმენით manual_join ფუნქცია
def manual_join(words):
    result = ""
    for i, word in enumerate(words):
        if i != 0:  
            result = result + " "
        result = result + word
    return result


