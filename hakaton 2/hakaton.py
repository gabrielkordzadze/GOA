# 3. Isogram Checker
# Description:
#  An isogram is a word with no repeating letters. Write a function to check if a string is an isogram (case insensitive).
# Example Test Cases:
# is_isogram("machine") → True


# is_isogram("letter") → False


# is_isogram("") → True

def is_isogram(a):
    a = a.lower() # აქ ვაქცევთ ყველა ასოს პატარად რადგან დიდი და პატარას შორის განსხვავება რომ არ იყოს
    for i in a:
        if a.count(i) > 1: #ვამოწმებთ თითოეულ ასოს თუ მეორდება გამოგვაქვს False
            return False
    return True #თუ არცერთი ასო მეორდება გამოაქვს True
        

print(is_isogram("letter"))
print(is_isogram("goa"))



# 5. Count by X
# Description:
#  Create a function that returns a list of the first n multiples of x.
# Example Test Cases:
# count_by(1, 5) → [1, 2, 3, 4, 5]


# count_by(2, 5) → [2, 4, 6, 8, 10]


# count_by(3, 4) → [3, 6, 9, 12]

def count(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(x * i)
    return result


print(count(2, 5))



# 1. Sum of Odd Numbers
# Description:
#  You are given an array of integers. Return the sum of only the odd numbers.
# Example Test Cases:
# sum_odds([1, 2, 3, 4, 5]) → 9


# sum_odds([2, 4, 6, 8]) → 0


# sum_odds([11, 21, 32, 43]) → 75


def sum_odds(num):
    total = 0
    for i in num:
        if i % 2 == 1:
            total += i
    return total 

print(sum_odds([1,2,3,4,5]))




# 2. Convert String to Camel Case
# Description:
#  Convert a string with hyphens or underscores to camel case. The first word should retain its case.
# Example Test Cases:
# to_camel_case("the_stealth_warrior") → "theStealthWarrior"


# to_camel_case("The-Stealth-Warrior") → "TheStealthWarrior"


# to_camel_case("") → ""


def to_camel_case(text):
    if text == "":
        return ""
    text = text.replace("-", "_") # ვცვლით დეფისს ("_")
    parts = text.split("_") # ვყოფთ სიტყვებად
    result = parts[0] # პირველი სიტყვა რჩება როგორც არის
    
    for word in parts[1:]: # მეორე სიტყვიდან ვიწყებთ
        result += word.capitalize() # ვამატებთ სიტყვას დიდი ასოთი
    return result


print(to_camel_case("The-Stealth-Warrior"))




# 6. Duplicate Encoder
# Description:
#  Convert each character in a string to '(' if it appears only once or to ')' if it appears more than once in the string (case insensitive).
# Example Test Cases:
# duplicate_encode("din") → "((("


# duplicate_encode("recede") → "()()()"


# duplicate_encode("Success") → ")())())"

def duplicate_encode(word):
    word = word.lower()
    result = ""
    for char in word:
        if word.count(char) == 1:
            result += "("
        else:
            result += ")"
    return result

print(duplicate_encode("din"))



# 7. Find the Odd Int
# Description:
#  Given an array of integers, find the one that appears an odd number of times.
# Example Test Cases:
# find_odd([20, 1, 1, 2, 2, 3, 3, 20, 4, 4, 5, 5, 5]) → 5


# find_odd([10, 10, 10]) → 10


# find_odd([1, 2, 3, 1, 2, 3, 1]) → 1


def find_odd(numbers):
    for num in numbers:
        if numbers.count(num) % 2 == 1:
            return num
        

print(find_odd([20, 1, 1, 2, 2, 3, 3, 20, 4, 4, 5, 5, 5]))




# 8. Format Phone Number
# Description:
#  Given a list of 10 integers, return a string in the form of a phone number: (123) 456-7890.
# Example Test Cases:
# create_phone_number([1,2,3,4,5,6,7,8,9,0]) → "(123) 456-7890"


# create_phone_number([0,0,0,0,0,0,0,0,0,0]) → "(000) 000-0000"


# create_phone_number([9,8,7,6,5,4,3,2,1,0]) → "(987) 654-3210"

def create_phone_number(numbers):
    part1 = ""
    part2 = ""
    part3 = ""

    for i in range(10):
        if i < 3:
            part1 += str(numbers[i])
        elif i < 6:
            part2 += str(numbers[i])
        else:
            part3 += str(numbers[i])
        

    return "(" + part1 + ") " + part2 + "-" + part3

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))



# 9. Counting Duplicates
# Description:
#  Count the number of distinct case-insensitive characters that occur more than once in a string.
# Example Test Cases:
# duplicate_count("abcde") → 0


# duplicate_count("aabbcde") → 2


# duplicate_count("aA11") → 2



def duplicate_count(text):
    text = text.lower()   # ტექსტს ვაქცევთ პატარა ასოებად
    counts = {}           # ცარიელი ლექსიკონი სიმბოლოების რაოდენობისთვის
    duplicates = 0        # ორჯერადი სიმბოლოების რაოდენობა

    for char in text:
        counts[char] = counts.get(char, 0) + 1  # თითო სიმბოლოს რიცხვის აღება და გაზრდა

    for count in counts.values():
        if count > 1:       # თუ სიმბოლო მეორდება, მივამატოთ რაოდენობას
            duplicates += 1

    return duplicates      # ვაბრუნებთ იმ სიმბოლოების რაოდენობას, რომლებიც მეორდება

print(duplicate_count("abcde"))
print(duplicate_count("aabbcde"))


# 10. Find the Parity Outlier
# Description:
#  Given an array of integers, where all but one are even or odd, find the outlier.
# Example Test Cases:
# find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) → 11


# find_outlier([160, 3, 1719, 19, 11, 13, -21]) → 160


# find_outlier([2, 6, 8, -10, 3]) → 3

def find_outlier(integers):
    even_count = 0
    odd_count = 0

    # პირველ 3 ელემენტში ვითვლით ლუწი/კენტის რაოდენობას
    for i in range(3):
        if integers[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # ვიგებთ რომელია სიიდან განსხვავებული — ლუწი თუ კენტი
    looking_for_even = odd_count > even_count

    # ახლა მთლიან სიაში ვეძებთ განსხვავებულს
    for num in integers:
        if looking_for_even and num % 2 == 0:
            return num
        if not looking_for_even and num % 2 != 0:
            return num




