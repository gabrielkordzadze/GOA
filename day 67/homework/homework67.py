# Jaden Casing Strings
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




# Beginner Series #3 Sum of Numbers
def get_sum(a,b):
    #good luck!
    if a == b:
        return a
    else:
        total = 0
        for i in range(min(a, b), max(a, b) + 1):
            total += i
        return total



# Maximum Length Difference
def mxdiflg(a1, a2):
    # your code
    mx = -1
    for x in a1:
        for y in a2:
            diff = abs(len(x) - len(y))
            if (diff > mx):
                mx = diff
    return mx



# Simple beads count
def count_red_beads(n):
    if n < 2:
        return 0
    return 2 * (n - 1)




# Simple Fun #136: Missing Values
def missing_values(seq):
    unique_numbers = list(set(seq))  # უნიკალური ელემენტების პოვნა
    x = y = None

    for num in unique_numbers:
        count = 0
        for item in seq:
            if item == num:
                count += 1
        if count == 1:
            x = num
        elif count == 2:
            y = num

    return x * x * y

