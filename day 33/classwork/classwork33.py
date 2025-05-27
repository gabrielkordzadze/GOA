#Volume of a Cuboid
def get_volume_of_cuboid(length, width, height):
    # Code goes here...
    return length * width * height


#Grasshopper - Array Mean
def find_average(nums):
    #your code here
    total_sum = 0  
    num_values = 0  
    
    for number in nums:
        total_sum += number  
        num_values += 1  
        
    if num_values == 0:
        return "List is empty, cannot calculate mean."
    else:
        return total_sum / num_values
    

#No zeros for heros
def no_boring_zeros(n):
    # your code
    if n == 0:
        return 0
    if n % 10 == 0:
        return no_boring_zeros(n // 10)
    return n


#Student's Final Grade
def final_grade(exam, projects):
    # final grade
    if exam > 90:
        return 100
    if projects > 10:
        return 100
    if exam > 75:
        if projects >= 5:
            return 90
    if exam > 50:
        if projects >= 2:
            return 75
    return 0


#Beginner - Lost Without a Map
def maps(a):
    result = []
    for i in a:
        result.append(i * 2)
    return result


