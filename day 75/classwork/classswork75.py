# Beginner Series #2 Clock
def past(h, m, s):
    # Good Luck!
        return (h * 3600 + m * 60 + s) * 1000


#A Needle in the Haystack
def find_needle(haystack):
    # your code here
    return "found the needle at position " + str(haystack.index("needle"))



#Beginner - Reduce but Grow
def grow(arr):
    result = 1
    for num in arr:
        result = result * num  # გამრავლება
    return result



#Transportation on vacation
def rental_car_cost(d):
    # your code
    cost_per_day = 40
    total = d * cost_per_day

    if d >= 7:
        total -= 50
    elif d >= 3:
        total -= 20

    return total


#Is this a triangle?
def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a


#Find the stray number
def stray(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num
        

# Sum of array singles
    total = 0
    for num in arr:
        if arr.count(num) == 1:
            total += num
    return total


#Sort Arrays (Ignoring Case)
def sortme(words):
    return sorted(words, key=str.lower)



#Hamming Distance
def hamming(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count



#Delete occurrences of an element if it occurs more than n times
def delete_nth(order,max_e):
    result = []
    counts = {}
    for num in order:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        
        if counts[num] <= max_e:
            result.append(num)
    return result

