# The Feast of Many Beasts
def feast(beast, dish):
    # your code here
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False
    

#Array plus array
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)


#All Star Code Challenge #18
def str_count(strng, letter):
    count = 0
    for char in strng:        
        if char == letter:    
            count += 1
    return count


#Summing a number's digits
def sum_digits(number):
    total = 0
    if number < 0: 
        number = -number  
    else:
        number = number  

    while number > 0:
        total += number % 10  
        number //= 10  

    return total



#Count characters in your string
def count(s):
    result = {}
    for i in s:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result



#Count Repeats
def count_repeats(txt):
    removals = 0
    for i in range(1, len(txt)):
        if txt[i] == txt[i-1]:
            removals += 1
    return removals



