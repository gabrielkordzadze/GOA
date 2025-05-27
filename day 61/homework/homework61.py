#List Filtering
def filter_list(l):
    result = []
    for x in l:
        if type(x) == int:  # თუ x არის მთელი რიცხვი
            result.append(x)  # დავამატოთ result სიაში
    return result  # დავაბრუნოთ გაფილტრული სია


#Exes and Ohs
def xo(s):
    s = s.lower()
    x_count = s.count('x')
    o_count = s.count('o')
    return x_count == o_count


#Shortest Word
def find_short(s):
    words = s.split()
    lengths = [len(word) for word in words]
    return min(lengths)


#Friend or Foe?
def friend(x):
    #Code
    result = []  # ცარიელი სია, სადაც შევინახავთ მეგობრების სახელებს
    for name in x:  # ვიქნებით თითოეული სახელი სიაში x
        if len(name) == 4:  # თუ სახელი 4 ასოზე შედგება
            result.append(name)  # დავამატებთ მას შედეგის სიაში
    return result  # დავაბრუნებთ საბოლოო შედეგს


#Two to One
def longest(a1, a2):
    # your code
    return ''.join(sorted(set(a1 + a2)))
               

