# Alternate capitalization
def capitalize(s):
    even = ''
    odd = ''
    for i in range(len(s)):
        if i % 2 == 0:
            even += s[i].upper()
            odd += s[i]
        else:
            even += s[i]
            odd += s[i].upper()
    return [even, odd]


#To square(root) or not to square(root)
def square_or_square_root(arr):
    result = []
    for num in arr:
        numb = int(num ** 0.5)
        if numb * numb == num:
            result.append(numb)
        else:
            result.append(num ** 2) 
    return result


#Sort Numbers
def solution(nums):
    if not nums:
        return []
    return sorted(nums)


#Testing 1-2-3
def number(lines):
    #your code here
    numbered_lines = []
    counter = 1
    for line in lines:
        numbered_lines.append(f"{counter}: {line}")
        counter += 1
    return numbered_lines



#Get Nth Even Number
def nth_even(n):
    #your code here
    return 2 * (n - 1)


#Odd or Even?
def odd_or_even(arr):
    if not arr:        # თუ სია ცარიელია
        arr = [0]      # ვაყენებთ [0]-ს
    total = sum(arr)   # ვთვლით ჯამს
    if total % 2 == 0:
        return "even"
    else:
        return "odd"
    


#Filter out the geese
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    #your code here
    filtered = []
    for bird in birds:
        if bird not in geese:
            filtered.append(bird)
    return filtered



#How many are smaller than me?
def smaller(arr):
    # Good Luck!
    result = []
    for i in range(len(arr)):
        count = 0
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                count += 1
        result.append(count)
    return result



#Reverse a Number
def reverse_number(n):
    if n < 0:
        reversed_str = str(-n)[::-1]
        return -int(reversed_str)
    else:
        reversed_str = str(n)[::-1]
        return int(reversed_str)
    

#Parts of a list
def partlist(arr):
    # your code
    result = []
    for i in range(1, len(arr)):
        left = " ".join(arr[:i])
        right = " ".join(arr[i:])
        result.append((left, right))
    return result


#Love vs friendship
def words_to_marks(s):
    # Easy one
    total = 0
    for i in s:
        total += ord(i) - ord('a') + 1
    return total


#Sum of Cubes
def sum_cubes(n):
    # your code here
    total = 0  
    for i in range(1, n + 1):
        total += i**3 
    return total 