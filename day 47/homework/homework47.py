#2)შეასრულეთ თქვენი არჩეული 3ცალი 8KYUანი ამოცანა

#Stringy Strings
def stringy(size):
    # Good Luck!
    result = ""
    for i in range(size):
        if i % 2 == 0:
            result += "1"
        else:
            result += "0"
    return result


#Return the day
def whatday(num):
  # Put your code here
    if num == 1:
        return "Sunday"
    elif num == 2:
        return "Monday"
    elif num == 3:
        return "Tuesday"
    elif num == 4:
        return "Wednesday"
    elif num == 5:
        return "Thursday"
    elif num == 6:
        return "Friday"
    elif num == 7:
        return "Saturday"
    else:
        return "Wrong, please enter a number between 1 and 7"
    



#No zeros for heroes
def no_boring_zeros(n):
    # your code
    if n == 0:
        return 0
    if n % 10 == 0:
        return no_boring_zeros(n // 10)
    return n


#3)შეასრულეთ თქვენი არჩეული 2ცალი 7KYUანი ამოცანა

#Sum of Cubes
def sum_cubes(n):
    # your code here
    total = 0  
    for i in range(1, n + 1):
        total += i**3 
    return total 



#Friend or Foe?
def friend(x):
    #Code
    result = [] 
    for name in x:  
        if len(name) == 4:  
            result.append(name)  
    return result

#4)შეასრულეთ თქვენი არჩეული 1ცალი 6KYUანი ამოცანა

#Sort the odd
def sort_array(source_array):
    odd_numbers = [] 
    for x in source_array:   
        if x % 2 != 0: 
            odd_numbers.append(x) 

    odd_numbers.sort() 

    odd_index = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:   
            source_array[i] = odd_numbers[odd_index] 
            odd_index += 1  

    return source_array





