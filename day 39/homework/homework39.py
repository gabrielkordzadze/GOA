#Returning Strings
def greet(name):
    #Good Luck (like you need it)
     return "Hello, " + name + " how are you doing today?"


#Sum Arrays
def sum_array(a):
    total = 0
    for num in a:
        total += num
    return total


#Basic Mathematical Operations
def basic_op(operator, value1, value2):
    #your code here
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    

#Convert a Number to a String!
def number_to_string(num):
    # Return a string of the number here!
    return str(num)
    

#Century From Year
def century(year):
    # Finish this :)
        return (year - 1) // 100 + 1