# Categorize New Member
def open_or_senior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result



# Small enough? - Beginner
def small_enough(array, limit):
    for number in array:
        if number > limit:
            return False
    return True