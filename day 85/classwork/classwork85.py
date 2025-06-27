#No zeros for heroes
def no_boring_zeros(n):
    # your code
    if n == 0:
        return 0
    if n % 10 == 0:
        return no_boring_zeros(n // 10)
    return n


#Convert to Binary
def to_binary(n):
    #your code here
    binary = ""
    if n == 0:
        return 0
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return int(binary)


# Gravity Flip
def flip(d, a):
    # Do some magic
    result = sorted(a)
    if d == 'L':
        result = result[::-1]  
    return result


#Count Repeats
def count_repeats(txt):
    removals = 0
    for i in range(1, len(txt)):
        if txt[i] == txt[i-1]:
            removals += 1
    return removals


#Hamming Distance
def hamming(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count


#What century is it?
def what_century(year):
    y = int(year)
    cent = (y + 99) // 100
    if 11 <= cent % 100 <= 13:
        suffix = "th"
    else:
        last_digit = cent % 10
        if last_digit == 1:
            suffix = "st"
        elif last_digit == 2:
            suffix = "nd"
        elif last_digit == 3:
            suffix = "rd"
        else:
            suffix = "th"
    return f"{cent}{suffix}"