# 8 kyu

#Convert a Boolean to a String
def boolean_to_string(b):
    #your code here
    return str(b)


#Array plus array
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)

#Twice as old
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)


# What is between?
def between(a,b):
    # good luck
    result = []
    for num in range(a, b + 1):
        result.append(num)
    return result


#Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    result = []
    for num in numbers:
        if num % divisor == 0:
            result.append(num)
    return result



# 7 kyu

#Descending Order
def descending_order(num):
    # Bust a move right here
    return int("".join(sorted(str(num), reverse=True)))


#Complementary DNA
def DNA_strand(dna):
    # code here
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in dna)


#Binary Addition
def add_binary(a,b):
    #your code here
    return bin(a + b)[2:]


# Shortest Word
def find_short(s):
    words = s.split()
    min_length = len(words[0])
    for word in words:
        if len(word) < min_length:
            min_length = len(word)
    return min_length



# List Filtering
def filter_list(l):
    result = []
    for x in l:
        if type(x) == int:  # თუ x არის მთელი რიცხვი
            result.append(x)  # დავამატოთ result სიაში
    return result  # დავაბრუნოთ გაფილტრული სია