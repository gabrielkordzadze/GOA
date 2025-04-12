#Get the mean of an array
def get_average(marks):
    total = sum(marks)         
    count = len(marks)         
    average = total // count   
    return average   


#Total amount of points
def points(games):
    total_points = 0
    for game in games:
        x, y = map(int, game.split(':'))
        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1
        
    return total_points


#Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    #your code here
    numbers.sort()
    return numbers[0] + numbers[1]


#Number of People in the Bus
def number(bus_stops):
    # Good Luck!
    total = 0
    for stop in bus_stops:
        total += stop[0] - stop[1]
    return total


#Build a square
def generate_shape(n):
    result = ''
    for i in range(n):
        for i in range(n):
            result += '+'
        result += '\n'
    return result[0:-1]


#Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0
    total = 0
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    return total

