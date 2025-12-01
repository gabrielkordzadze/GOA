# 1) https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
def solution(number):
    if number < 0:
        return 0
    total = 0
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    return total

# 2) https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
def array_diff(a, b):
    result = []
    for x in a:
        if x not in b:
            result.append(x)
    return result
            

# 3) https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
def spin_words(sentence):
    # Your code goes here
    words = sentence.split()  # Split sentence into words
    result = []

    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])  # Reverse word if length >= 5
        else:
            result.append(word)  # Keep it unchanged

    return ' '.join(result)  # Reconstruct the sentence

# 4) https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
def digital_root(n):
    return 0 if n == 0 else 1 + (n - 1) % 9
