#Vowel Count
def get_count(sentence):
    vowels = "aeiou"  
    vowel_count = 0    

    for letter in sentence:
        if letter in vowels:  
            vowel_count += 1  

    return vowel_count


#Shortest Word
def find_short(s):
    words = s.split()
    min_length = len(words[0])
    for word in words:
        if len(word) < min_length:
            min_length = len(word)
    return min_length


#Stones on the Table
def solution(stones):
    # Do some magic
    count = 0
    i = 1
    while i < len(stones):
        if stones[i] == stones[i - 1]:
            count += 1
        i += 1
    return count
   


#Disemvowel Trolls
def disemvowel(string_):
    vowels = "aeiouAEIOU"  # ხმოვანი ასოები (A, E, I, O, U და მათი დიდი ვერსიები)
    result = ""  # შედეგი, სადაც შევინახავთ სიმბოლოებს

    for char in string_:  # თითოეული სიმბოლოსთვის გავდივართ სტრიქონში
        if char not in vowels:  # თუ სიმბოლო არ არის ხმოვანი
            result += char  # დავამატოთ სიმბოლო შედეგში

    return result  # ვაბრუნებთ საბოლოო შედეგს



#Highest and Lowest
def high_and_low(numbers):
    # სტრიქონიდან ვყაზავთ ცალკე რიცხვებს
    num_list = numbers.split()  # სტრიქონს ვყაზავთ რიცხვებად, რომლებიც ერთმანეთთან არიან გაყოფილი Space-ით
    highest = int(num_list[0])  # პირველ რიცხვს ვანიჭებთ მაქსიმუმს
    lowest = int(num_list[0])   # პირველ რიცხვს ვანიჭებთ მინიმუმს

    # თითოეული რიცხვისთვის გადის ციკლი
    for num in num_list:
        num = int(num)  # რიცხვი ცვლება int-ად, რომ შევძლოთ შედარება
        if num > highest:  # თუ რიცხვი მეტია მაქსიმუმზე
            highest = num  # მაშინ, ის ხდება ახალი მაქსიმუმი
        if num < lowest:   # თუ რიცხვი ნაკლებია მინიმუმზე
            lowest = num   # მაშინ, ის ხდება ახალი მინიმუმი

    # შედეგი ფორმატირებული სტრიქონის სახით, სადაც პირველ ადგილზე მაქსიმუმია, მეორე ადგილზე მინიმუმი
    return f"{highest} {lowest}"




#Square Every Digit
def square_digits(num):
    result = ""  # შედეგი იქნება სტრიქონი, სადაც ჩაწერილი იქნება ყველა კვადრატი

    for digit in str(num):  # გადავდივართ ყველა ციფრზე (ციფრი სტრიქონის სახით)
        square = int(digit) ** 2  # ციფრის კვადრატი
        result += str(square)  # ვამატებთ კვადრატს სტრიქონში

    return int(result)  # ვაბრუნებთ საბოლოო რიცხვს როგორც int

