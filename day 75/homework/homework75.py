#You're a square!
def is_square(n):    
    if n < 0:
        return False
    x = 0
    while x * x <= n:
        if x * x == n:
            return True
        x += 1
    return False



#Get the Middle Character
def get_middle(s):
    length = len(s)
    middle = length // 2
    if length % 2 == 0:
        return s[middle - 1:middle + 1]
    else:
        return s[middle]
    


#String ends with?
def solution(text, ending):
    # your code here...
    return text.endswith(ending)


#Complementary DNA
def DNA_strand(dna):
    # code here
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna)


#Binary Addition
def add_binary(a,b):
    #your code here
    return bin(a + b)[2:]


#Categorize New Member
def open_or_senior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result




#Find the next perfect square!
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    root = sq ** 0.5
    if root.is_integer():
        next_root = int(root) + 1
        return next_root * next_root
    else:
        return -1
    



#Growth of a Population
def nb_year(p0, percent, aug, p):
    # your code
    years = 0
    while p0 < p:
        p0 = int(p0 + p0 * (percent / 100) + aug)
        years += 1
    return years



#Ones and Zeros
def binary_array_to_number(arr):
  # your code
    number = 0
    for bit in arr:
        number = number * 2 + bit
    return number



#Odd or Even?
def odd_or_even(arr):
    total = sum(arr) if arr else 0
    return "even" if total % 2 == 0 else "odd"


#Sum of the first nth term of Series
def series_sum(n):
    # Happy Coding ^_^
    if n == 0:
        return "0.00"
    
    total = 0.0
    for i in range(n):
        total += 1 / (1 + 3 * i)
    
    return f"{total:.2f}"



#Find the divisors!
def divisors(integer):
    result = []
    for i in range(2,integer):
        if n % i == 0:
            result.append(i)
    if not result:
        return f"{integer} is prime"
    return result



#Remove the minimum
def remove_smallest(numbers):
    if not numbers:
        return []
    min_index = numbers.index(min(numbers))
    return numbers[:min_index] + numbers[min_index+1:]



#Testing 1-2-3
def number(lines):
    #your code here
    numbered_lines = []
    counter = 1
    for line in lines:
        numbered_lines.append(f"{counter}: {line}")
        counter += 1
    return numbered_lines


#Count the divisors of a number
def divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1  
            else:
                count += 2  
        i += 1
    return count