#Make a function that does arithmetic!
def arithmetic(a, b, operator):
    #your code here
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b
    }
    return operations[operator]



#Anagram Detection
# write the function is_anagram
def is_anagram(test, original):
    test_sorted = sorted(test.lower())
    original_sorted = sorted(original.lower())

    if test_sorted == original_sorted:
        return True
    else:
        return False
    




#Count by X
def count_by(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(x * i)
    return result



#Third Angle of a Triangle
def other_angle(a, b):
    return 180 - (a + b)


#Sum even numbers
def sum_even_numbers(seq): 
    # your code here
    total = 0
    for num in seq:
        if num % 2 == 0 and num == int(num):
            total += num
    return total



#Cat years, Dog years
def human_years_cat_years_dog_years(human_years):
    # Your code here
    cat_years = 0
    dog_years = 0
    
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5
        
    return [human_years, cat_years, dog_years]



#Sum The Strings
def sum_str(a, b):
    # happy coding !
    return str(int(a or 0) + int(b or 0))



#Remove the minimum
def remove_smallest(numbers):
    if not numbers:
        return []
    min_index = numbers.index(min(numbers))
    return numbers[:min_index] + numbers[min_index+1:]