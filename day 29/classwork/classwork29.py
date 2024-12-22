#1)შექმენით ფუნქცია რომელსაც გადაეცემა სია,გამოითვალეთ რიცხვების ჯამი for ციკლის საშუალებითაც და sum() ფუნქციის გამოყენებითაც აუცილებლად დააბრუნეთ შედეგი return ის გამოყენებით.
def calculate_sum(numbers):
    total_for = 0
    for num in numbers:
        total_for += num



def sum(number):
    sum = 0
    for i in number:
         sum += i
         return sum
   

print(sum([1,2,3,4,5]))
  
    