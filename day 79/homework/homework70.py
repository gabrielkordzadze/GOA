#Reversed Strings
def solution(string):
    return string[::-1]


#Sum Arrays
def sum_array(a):
    total = 0
    for num in a:
        total += num
    return total


#Unique In Order
def unique_in_order(sequence):
    result = []
    prev = object()  
    for item in sequence:
        if item != prev:
            result.append(item)
            prev = item
    return result



#IP Validation
def is_valid_IP(strng):
    parts = strng.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if len(part) > 1 and part[0] == '0':
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True