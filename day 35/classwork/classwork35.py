#Find the capitals
def capitals(word):
    #your code here
    indices = []  # შევქმნათ ცარიელი სია, სადაც ჩავდებთ ინდექსებს
    for i in range(len(word)):  # ვადევნებთ თვალს სტრიქონის თითოეულ ასოს
        if word[i].isupper():  # თუ ასო არის დიდი (uppercase)
            indices.append(i)  # მისი ინდექსი დამატებული იქნება სიაში
    return indices  # დავაბრუნოთ ინდექსები



#Maximum Multiple
def max_multiple(divisor, bound):

    #your code here
    for i in range(bound, 0, -1):
        # თუ i მთლიანად იყოფა divisor-ით, მაშინ ის არის ჩვენი შედეგი
        if i % divisor == 0:
            return i  # ვბრუნდებით პირველივე რიცხვზე, რომელიც შეესაბამება მოთხოვნებს
        

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




