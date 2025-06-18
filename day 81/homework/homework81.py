#Convert PascalCase string into snake_case
def to_underscore(strng: str) -> str:
    # your code here
    if isinstance(strng, int):
        return str(strng)
    
    result = ""
    for i, char in enumerate(strng):
        if char.isupper() and i != 0:
            result += "_"
        result += char.lower()
    return result


#Bit Counting
def count_bits(n):
    return bin(n).count("1")


#Kebabize
def kebabize(st):
    #your code here
    result = ""
    for char in st:
        if char.isdigit():
            continue  # ციფრებს გამოტოვებს
        if char.isupper():
            if result:  # თუ უკვე რაღაც არის, ჰიფენს დებს
                result += "-"
            result += char.lower()
        else:
            result += char
    return result



#Where is my parent!?(cry)
def find_children(dancing_brigade):
    result = ""
    mothers = sorted([ch for ch in dancing_brigade if ch.isupper()])
    
    for mother in mothers:
        children = mother.lower() * dancing_brigade.count(mother.lower())
        result += mother + children
    return result