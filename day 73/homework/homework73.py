#Count characters in your string
def count(s):
    result = {}
    for i in s:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result



#The Vowel Code
def encode(st):
    result = ""
    for i in st:
        if i == 'a':
            result += '1'
        elif i == 'e':
            result += '2'
        elif i == 'i':
            result += '3'
        elif i == 'o':
            result += '4'
        elif i == 'u':
            result += '5'
        else:
            result += i
    return result
    
def decode(st):
    result = ""
    for i in st:
        if i == '1':
            result += 'a'
        elif i == '2':
            result += 'e'
        elif i == '3':
            result += 'i'
        elif i == '4':
            result += 'o'
        elif i == '5':
            result += 'u'
        else:
            result += i
    return result



# Handshake problem
def get_participants(handshakes):
    for i in range(handshakes + 2): 
        if i * (i - 1) // 2 >= handshakes:
            return i



# Sort Arrays (Ignoring Case)
def sortme(words):
    return sorted(words, key=str.lower)