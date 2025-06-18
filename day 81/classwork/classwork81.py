#Super Duper Easy
def problem(a):
    #Easy Points ^_^
    if type(a) == str:
        return "Error"
    return a * 50 + 6


#They say that only the name is long enough to attract attention. They also said that only a simple Kata will have 
# someone to solve it. This is a sadly story #1: Are they opposite?
def is_opposite(s1,s2):
    if not s1 or not s2:
        return False
    if len(s1) != len(s2):
        return False
    for c1, c2 in zip(s1, s2):
        if c1.lower() != c2.lower() or c1 == c2:
            return False
    return True


#Flick Switch
def flick_switch(lst):
    result = []
    state = True
    for item in lst:
        if item == 'flick':
            state = not state
        result.append(state)
    return result


#Chuck Norris VII - True or False? (Beginner)
def if_chuck_says_so():
    # code here
    return 1 == 0


#Moving Zeros To The End
def move_zeros(lst):
    result = []
    zero_count = 0

    for x in lst:
        if x == 0:
            zero_count += 1
        else:
            result.append(x)

    for _ in range(zero_count):
        result.append(0)

    return resul



#Simple Pig Latin
def pig_it(text):
    #your code here
    result = []
    for word in text.split():
        if word.isalpha():
            result.append(word[1:] + word[0] + 'ay')
        else:
            result.append(word)
    return ' '.join(result)


#Extract the domain name from a URL
def domain_name(url):
    url = url.replace("https://", "").replace("http://", "").replace("www.", "")
    domain = url.split("/")[0]
    return domain.split(".")[0]


#Not very secure
def alphanumeric(password):
    if password == "":
        return False
    
    for char in password:
        if not char.isalnum():
            return False
    
    if ' ' in password or '_' in password:
        return False

    return True