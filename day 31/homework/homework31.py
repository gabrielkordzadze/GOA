#Function 1 - hello world
# Write a function `greet` that returns "hello world!"
def greet():
    return "hello world!"

#Opposite number
def opposite(number):
  # your solution here
    return -number

#Return Negative
def make_negative( number ):
    if number > 0:
        return -number
    return number

#Sum of positive
def positive_sum(arr):
    # Your code here
    total = 0
    for num in arr:
        if num > 0:
            total += num 
    return total

#String repeat
def repeat_str(repeat, string):
     return repeat * string

#Square(n) Sum
def square_sum(numbers):
    #your code here
    total = 0
    for i in numbers:
        total += i ** 2
    return total

#Find the smallest integer in the array
def find_smallest_int(arr):
    # Code here
    return min(arr)

#Grasshopper - Summation
def summation(num):
    
     # Code here
    total = 0
    for i in range(1, num + 1):
        total += i
    return total
    
#Remove String Spaces
def no_space(x):
    #your code here
    result = ""
    for i in x:
        if i != " ":
            result += i
    return result

#Counting sheep...
def count_sheeps(sheep):
  # TODO May the force be with you
    count = 0
    for s in sheep:
        if s: 
            count += 1
    return count




