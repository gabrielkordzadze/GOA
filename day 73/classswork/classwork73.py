# Printer Errors
def printer_error(s):
    errors = 0
    for i in s:
        if i > 'm':
            errors += 1
    return f"{errors}/{len(s)}"


#Number of People in the Bus
def number(bus_stops):
    # Good Luck!
    total = 0
    for stop in bus_stops:
        total += stop[0] - stop[1]
    return total



#Don't give me five
def dont_give_me_five(start, end):
    count = 0
    for num in range(start, end + 1):
        check_num = num
        if check_num <0:
            check_num = - check_num
        fives = 0
        while check_num > 0:
            if check_num % 10 == 5:
                fives = 1
            check_num //= 10
        if fives == 0:
            count += 1
    return count







#Array.diff
def array_diff(a, b):
    result = []
    for x in a:
        if x not in b:
            result.append(x)
    return result



#Take a Ten Minutes Walk
def is_valid_walk(walk):
    #determine if walk is valid
    if len(walk) != 10:
        return False

    north = walk.count('n')
    south = walk.count('s')
    east = walk.count('e')
    west = walk.count('w')

    if north == south and east == west:
        return True
    else:
        return False
    


#Sum of Digits / Digital Root
def digital_root(n):
    return 0 if n == 0 else 1 + (n - 1) % 9



#Unique In Order
def unique_in_order(sequence):
    result = []
    prev = object()  
    for item in sequence:
        if item != prev:
            result.append(item)
            prev = item
    return result
    