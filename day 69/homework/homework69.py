# Create Phone Number
def create_phone_number(n):
    #your code here
    phone="({}{}{}) {}{}{}-{}{}{}{}"
    return (phone.format(*n))


# Find the odd int
def find_it(seq):
    result = 0
    for num in seq:
        result ^= num
    return result

#Array.diff
def array_diff(a, b):
    result = []  
    for x in a: 
        if x not in b:  
            result.append(x)  
    return result


#Is it a palindrome?
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


#Was the package received before it was sent? (Simplified)
def was_package_received_yesterday(tz_from, tz_to, start, duration):
    return start < tz_from - tz_to - duration
