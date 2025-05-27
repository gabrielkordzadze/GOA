#1)შექმენით ფუნქცია სახელად sum, რომელსაც გადაეცემა რიცხვების სია და თქვენი დავალებაა დაბეჭდოთ ამ სიაში მყოფი ყველა რიცხვის ჯამი
def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)

sum([1, 2, 3, 4, 5])