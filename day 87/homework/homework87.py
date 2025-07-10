# 8 kyu

#Sum Arrays
def sum_array(a):
    total = 0
    for num in a:
        total += num
    return total



#Thinkful - Number Drills: Blue and red marbles
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    # Your code here.
    remaining_blue = blue_start - blue_pulled
    remaining_red = red_start - red_pulled
    return remaining_blue / (remaining_blue + remaining_red)



#Grasshopper - Terminal game move function
def move(position, roll):
    # your code here
    return position + roll * 2



#Is it a palindrome?
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]



#Twice as old
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)




# 7 kyu

#Balance the parentheses
def fix_parentheses(strng):
    open_needed = 0
    extra_closing = 0

    for char in strng:
        if char == '(':
            open_needed += 1
        else:  # char == ')'
            if open_needed > 0:
                open_needed -= 1
            else:
                extra_closing += 1

    return '(' * extra_closing + strng + ')' * open_needed


#String prefix and suffix
def solve(st):
    max_len = 0
    n = len(st)
    for length in range(1, n // 2 + 1):
        if st[:length] == st[-length:]:
            max_len = length
    return max_len


#Binary Addition
def add_binary(a,b):
    #your code here
    return bin(a + b)[2:]



#Shortest Word
def find_short(s):
    words = s.split()
    min_length = len(words[0])
    for word in words:
        if len(word) < min_length:
            min_length = len(word)
    return min_length



#Ones and Zeros
def binary_array_to_number(arr):
  # your code
    number = 0
    for bit in arr:
        number = number * 2 + bit
    return number



# 6 kyu

#Death by Coffee
def coffee_limits(year, month, day):
    # დაბადების რიცხვი 8-ნიშნა ფორმატით: YYYYMMDD
    h = int(f"{year:04d}{month:02d}{day:02d}")
    
    REGULAR = 0xCAFE   # 51966
    DECAF = 0xDECAF    # 912559
    
    def contains_dead(n):
        return "DEAD" in hex(n).upper()
    
    def get_limit(coffee_value):
        health = h
        for cups in range(1, 5001):
            health += coffee_value
            if contains_dead(health):
                return cups
        return 0
    
    return [get_limit(REGULAR), get_limit(DECAF)]



#Find the odd int
def find_it(seq):
    result = 0
    for num in seq:
        result ^= num
    return result