# Will my horse make it to the end?
def estimator(s,o):
    i=0
    while i<len(s):
        if s[i]==1:
            a=0
            while i+a<len(s) and s[i+a]==1:
                a+=1
            if a==1:
                o-=2
            elif a==2:
                o-=5
            elif a==3:
                o-=10
            if o<0:
                return False
            i+=a
        else:
            i+=1
    return True



# The Speed of Letters
def speedify(s): 
    lst = [' '] * (len(s)+26)
    for i,c in enumerate(s):
        lst[i+ord(c)-65] = c
    return ''.join(lst).rstrip()


#List Filtering
def filter_list(l):
    result = []
    for x in l:
        if type(x) == int:
            result.append(x)
    return result



# Delete occurrences of an element if it occurs more than n times
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
