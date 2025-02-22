#Take the Derivative
def derive(coefficient, exponent): 
    # your code here
    result = coefficient * exponent
    
    exponent -= 1
    
    return str(result) + "x^" + str(exponent)


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
    


#Unfinished Loop - Bug Fixing #1
def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]  
        i += 1  
    return res



#Leap Years
def is_leap_year(year):
    #your code here. Try to do it in one line.
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False
    

