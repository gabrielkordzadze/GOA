#Summing a number's digits
def sum_digits(number):
    total = 0
    if number < 0:  # თუ რიცხვი ნეგატიურია
        number = -number  # ნეგატიური რიცხვი დადებითად გადავაქციოთ
    else:
        number = number  # სხვა შემთხვევაში, რიცხვი უკვე დადებითია

    # ციფრების დამატება ჯამში
    while number > 0:
        total += number % 10  # ბოლო ციფრის დამატება
        number //= 10  # რიცხვის ციფრის ამოღება

    return total



#Search for letters
def change(st):
    st = st.lower()  
    result = ['0'] * 26  

    for char in st:
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a') 
            result[index] = '1'  
            
    return ''.join(result)



#Sort the Gift Code
def sort_gift_code(code):
    return ''.join(sorted(code))


#Stop gninnipS My sdroW!
def spin_words(sentence):
    # Your code goes here
    words = sentence.split() 
    result = []

    for word in words:
        if len(word) >= 5:
            result.append(word[::-1]) 
        else:
            result.append(word)  

    return ' '.join(result)  