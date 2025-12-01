#Will my horse make it to the end?
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


#The Speed of Letters
def speedify(s): 
    lst = [' '] * (len(s)+26)
    for i,c in enumerate(s):
        lst[i+ord(c)-65] = c
    return ''.join(lst).rstrip()



#Simple Fun #136: Missing Values
def missing_values(seq):
    unique_numbers = list(set(seq))  # უნიკალური ელემენტების პოვნა
    x = y = None

    for num in unique_numbers:
        count = 0
        for item in seq:
            if item == num:
                count += 1
        if count == 1:
            x = num
        elif count == 2:
            y = num

    return x * x * y


#Search for letters
def change(st):
    st = st.lower()  
    result = ['0'] * 26  

    for char in st:
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a') 
            result[index] = '1'  
            
    return ''.join(result)



#Bit Counting
def count_bits(n):
    return bin(n).count("1")



#Count Repeats
def count_repeats(txt):
    removals = 0
    for i in range(1, len(txt)):
        if txt[i] == txt[i-1]:
            removals += 1
    return removals
