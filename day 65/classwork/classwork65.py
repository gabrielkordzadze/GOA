#Exclamation marks series #2: Remove all exclamation marks from the end of sentence
def remove(st):
    new_st = ""
    found_end = False
    for i in range(len(st)- 1, -1, -1):
        if not found_end and st[i] != "!":
            found_end = True
        if found_end:
            new_st = st[i] + new_st
    return new_st


#Fix the loop!
def list_animals(animals):
    result = ""
    for i in range(len(animals)):
        result += f"{i + 1}. {animals[i]}\n"
    return result


#Breaking chocolate problem
def break_chocolate(n, m):
    if n < 1 or m < 1:
        return 0
    return n * m - 1


#Anagram Detection
# write the function is_anagram
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())


#Are the numbers in order?
def in_asc_order(arr):
    # random_ is not allowed
     return arr == sorted(arr)


#Flatten and sort an array
def flatten_and_sort(array):
    flat = []
    for sublist in array:
        for num in sublist:
            flat.append(num)
    flat.sort()
    return flat
