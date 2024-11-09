#1)მომხმარებელს შემოატანინეთ მისი სახელი და თუ ეს სახელი უდრის თქვენს სახელს, დაბეჭდეთ "Hello" სხვა შემთხვევაში "Bye".
name = input("enter your name:")
if name == "gabo":
    print("hello")

else:
    print("bye")


#2)ცვლადში შეინახეთ თქვენი საყვარელი რიცხვი და მომხმარებელს შემოატანინეთ ასევე მისი საყვარელი რიცხვი, თუ თქვენი რიცხვები ემთხვევა მაშინ 
# დაბეჭდეთ "Perfect" თუ მისი რიცხვი მეტია, დაბეჭდეთ "More", სხვა შემთხვევაში "Less".

favnum = 8

herfavnum = int(input("enter your fav num:"))
if herfavnum == favnum:
    print("perfect")


if herfavnum > favnum:
    print("more")


else:
    print("less")


#3)შექმენით for ციკლი 150ის დიაპაზონში და შეამოწმეთ თითოეული რიცხვი, თუ ეს რიცხვი არის ლუწი, მაშინ დაბეჭდეთ "Luwia" და გვერძე
#  მიაწერეთ რიცხვი (მინიშნება ---> print("Luwia", i) ხოლო თუ იქნება კენტი, დაბეჭდეთ "Kentia" და გვერძე მიუწერეთ ეს რიცხვი.

for i in range(150):
    if i % 2 == 0:
        print("luwia",i)

else:
    print("kentia",i)



#4)მომხმარებელს შემოატანინეთ მისი ასაკი და ასევე მისი სახელი, თუ მომხმარებლის
#  სახელი ემთხვევა თქვენს სახელს და ასევე მისი ასაკი ემთხვევა თქვენს სახელს, დაბეჭდეთ 
# "Twins" სხვა შემთხვევაში "Not Twins".

my_name = "gabrieli"
my_age = 13

user_name = input("enter your name:")
user_age = int(input("enter your age:"))

if user_name == my_name and user_age == my_age:
    print("twins")
else:
    print("not twins")


#5)შექმენით ცვლადი სადაც შეინახავთ ორიგინალ აქაუნთის პაროლს, და while ციკლის მეშვეობით მომხმარებელს
#  შეეკითხეთ აქაუნთის პაროლი იქამდე სანამ სწორედ არ გამოიცნობს.

original_password = "password 123"

while True:
    user_password = input("enter your password:")
    if user_password == original_password:
        print("password is succes")
        break
    
else:
    print("password isnt succes")