# Who likes it?
def likes(names):
    # your code here
    count = len(names)
    if count == 0:
        return "no one likes this"
    elif count == 1:
        return f"{names[0]} likes this"
    elif count == 2:
        return f"{names[0]} and {names[1]} like this"
    elif count == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {count - 2} others like this"




#Create Phone Number
def create_phone_number(n):
    #your code here
    phone="({}{}{}) {}{}{}-{}{}{}{}"
    return (phone.format(*n))



#Find the odd int
def find_it(seq):
    result = 0
    for num in seq:
        result ^= num
    return result


#Largest pair sum in array
def largest_pair_sum(numbers): 
    # your code here
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    numbers.remove(max2)
    return max1 + max2



#Row Weights
def row_weights(array):
    team1 = sum(array[::2])  
    team2 = sum(array[1::2])
    return team1, team2