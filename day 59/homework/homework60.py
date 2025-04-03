#The highest profit wins!
def min_max(lst):
    return [min(lst), max(lst)]


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




#Fizz Buzz
def fizzbuzz(n):
    result = []  # ვქმნით ცარიელ სიას, სადაც შევინახავთ შედეგებს
    for i in range(1, n + 1):  # ვიცავთ ციკლს 1-დან n-მდე
        if i % 3 == 0 and i % 5 == 0:  # თუ რიცხვი არის 3-ის და 5-ის ჯერადი
            result.append("FizzBuzz")  # "FizzBuzz" შევიტანოთ სიაში
        elif i % 3 == 0:  # თუ რიცხვი მხოლოდ 3-ის ჯერადი
            result.append("Fizz")  # "Fizz" შევიტანოთ სიაში
        elif i % 5 == 0:  # თუ რიცხვი მხოლოდ 5-ის ჯერადი
            result.append("Buzz")  # "Buzz" შევიტანოთ სიაში
        else:
            result.append(i)  # თუ სხვა რიცხვია, უბრალოდ რიცხვი შევიტანოთ სიაში
    return result  # დავაბრუნოთ "result" სია


#Simple Fun #136: Missing Values
def missing_values(seq):
    unique_numbers = list(set(seq)) 
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
