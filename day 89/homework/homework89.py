#boss level
#Largest 5 digit number in a series
def solution(digits):
    max_seq = 0
    for i in range(len(digits) - 4):
        current_seq = int(digits[i:i+5])
        if current_seq > max_seq:
            max_seq = current_seq
    return max_seq


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