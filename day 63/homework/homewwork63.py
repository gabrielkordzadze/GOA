#Isograms
def is_isogram(string):
    #your code here
    string = string.lower()
    return len(string) == len(set(string))


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


#Mumbling
def accum(st):
    result = []  

    for i in range(len(st)):
        letter = st[i]                  
        part = letter.upper() + letter.lower() * i 
        result.append(part)              
    return "-".join(result)



#Regex validate PIN code
def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6:
        return False
    
    if not pin.isdigit():
        return False

    return True




#Sum of odd numbers
def row_sum_odd_numbers(n):
    #your code here
    return n ** 3