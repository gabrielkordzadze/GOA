#1)გააგრძელეთ ამ ქოუდვარსების შესრულება და გააკეთეთ მინიმუმ 10  8 კიუანი ამოცანა 

#Abbreviate a Two Word Name
def abbrev_name(name):
    first_initial = name[0].upper()  
    second_initial = name[name.index(" ") + 1].upper()  
    
    return first_initial + "." + second_initial 


#Convert number to reversed array of digits
def digitize(n):
    result = []
    for digit in str(n):
        result.insert(0, int(digit))
    return result


#Opposites Attract
def lovefunc( flower1, flower2 ):
    # ...
    return (flower1 % 2 != flower2 % 2)


#Beginner Series #1 School Paperwork
def paperwork(n, m):
    # Happy Coding! ^_^
    if n < 0 or m < 0:
        return 0
    return n * m


#Beginner Series #2 Clock
def past(h, m, s):
    # Good Luck!
        return (h * 3600 + m * 60 + s) * 1000


#Is he gonna survive?
def hero(bullets, dragons):
    return bullets >= dragons * 2


#Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    if len(arr) == 0:  # Check if the array is empty
        return []
    
    count_positives = 0
    sum_negatives = 0
    
    for num in arr:
        if num > 0:
            count_positives += 1
        elif num < 0:
            sum_negatives += num
    
    return [count_positives, sum_negatives]



#Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
     return mpg * fuel_left >= distance_to_pump