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


#The Hashtag Generator
def generate_hashtag(s):
    #your code here
    words = s.strip().split()
    if not words:
        return False
    hashtag = "#"
    for word in words:
        hashtag += word.capitalize()
    return hashtag if len(hashtag) <= 140 else False

#Count Repeats
def count_repeats(txt):
    removals = 0
    for i in range(1, len(txt)):
        if txt[i] == txt[i-1]:
            removals += 1
    return removals