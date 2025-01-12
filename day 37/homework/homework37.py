#Remove First and Last Character Part Two
def array(string):
    #your code here
    items = string.split(',')
    
    if len(items) <= 2:
        return None
    
    return ' '.join(items[1:-1])


#Template Strings
def temple_strings(obj, feature): 
    # your code here
    return obj + " are " + feature


#Contamination #1 -String-
def contamination(text, char):
    if text == "" or char == "":
        return ""
    return char * len(text)


#Is it a palindrome?
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


#Email Address Obfuscator
def obfuscate(email):
    email = email.replace('@', ' [at] ')
    email = email.replace('.', ' [dot] ')
    return email