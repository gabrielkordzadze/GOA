#Generate range of integers
def generate_range(start, stop, step):
    result = []
    for i in range(start, stop + 1, step):
        result.append(i)
    return result


#reverseIt
def reverse_it(data):
    if type(data) == str:  
        return data[::-1] 
    elif type(data) == int: 
        return int(str(data)[::-1])
    elif type(data) == float: 
        return float(str(data)[::-1])  
    return data