#Thinkful - Logic Drills: Traffic light
def update_light(current):
    # Your code here.
    if current == "green":
        return "yellow"
    if current == "yellow":
        return "red"
    if current == "red":
        return "green"
    

#Count by X
def count_by(x, n):
    result = []
    for i in range(1, n + 1):
        result.append(x * i)
    return result


#Abbreviate a Two Word Name
def abbrev_name(name):
    first_initial = name[0].upper()  
    second_initial = name[name.index(" ") + 1].upper()  
    
    return first_initial + "." + second_initial


#Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    if len(arr) == 0:  # Check if the array is empty
        return []
    
    count_positives = 0
    sum_negatives = 0
    
    for num in arr:
        if num > 0:
            count_positives += 1
        elif num < 0:
            sum_negatives += num
    
    return [count_positives, sum_negatives]


#Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"