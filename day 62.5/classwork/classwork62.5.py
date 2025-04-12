#4) შექმენით manual_len ფუნქცია "ფუნქციაში არ უნდა გამოიყენოთ len()"
def manual_len(obj):
    count = 0
    for item in obj:
        count += 1
    return count

print(manual_len([1, 2, 3, 4]))  
print(manual_len("hello"))
print(manual_len("GOA is the best academy"))