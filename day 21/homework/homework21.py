#1)კომენტარებით ახსენით განსხვევება indexing-სა და sliceing-ს შორის.
#ინდექსირება გამოიყენება ერთ კონკრეტულ ელემენტზე წვდომისთვის, ხოლო სლაისინგი საშვალებას გვაძლევს რაღაც სტრუქტურიგან ამოვიღოთ ელემენტთა ჯგუფი


#2)შექმენით სია სადაც გექნებათ 5 ელემენტი და მინუს ინდექსების გამოყენებით გამოიტანეთ ბოლო 3 ელემენტი

name = ["gabo","zauri","saba","vano","aleqsi"]
print(name[-3:])

#3)შექმენით სია სადაც გექნებათ 10 რიცხვი, გადაუარეთ ამ სიას და გამოიტანეთ მხოლოდ ის რიცხვები რომელიც მეტია ან ტოლია 10ზე
numbers = [20,10,2,55,13,4,78,11,12,33]
for i in numbers:
    if i >= 10:
        print(i)


#4)კომენტარის სახით ახსენით რა არის ფუქნცია, რაში ვიყენებთ და ჩამოწერეთ ყველა ნასწავლი ფუნქცია (გვერდით მიუწერეთ მათი დანიშნულება)

#ფუნქცია არის კოდის ნაწილი რომელსაც აქვს სახელი და რომელიც შეგვიძლია რამდენჯერმე გამოვიყენოთ ის საშვალებას გვაძლევს ავირიდოთ ერთი
#  და იგიე კოდის განმეორება და გავამარტივოთ მუშაობა

#1. print()

#დანიშნულება: მონაცემის ეკრანზე გამოჩენა.
#მაგალითი:

print("გამარჯობა, სამყარო!") 



#2. input()

#დანიშნულება: მომხმარებლისგან მონაცემის შეყვანა.
#მაგალითი:

name = input("შეიყვანეთ თქვენი სახელი: ")
print("გამარჯობა,", name)






#3. type()

#დანიშნულება: ობიექტის ტიპის დაბრუნება.
#მაგალითი:

print(type(10))  # შედეგი: <class 'int'>
print(type("ტექსტი"))  # შედეგი: <class 'str'>



#3. range()

#დანიშნულება: თანმიმდევრული რიცხვების გენერირება (მარტივად, ციკლში გამოსაყენებლად).
#მაგალითი:

for i in range(3):
    print(i)  # შედეგი: 0, 1, 2



#4. int() / float() / str()

#დანიშნულება: მონაცემის ტიპის გადაყვანა.
#მაგალითი:

num = "123"
print(int(num) + 1)  # შედეგი: 124



#5. sum()

#დანიშნულება: სიის ყველა ელემენტის ჯამის გამოთვლა.
#მაგალითი:

numbers = [1, 2, 3]
print(sum(numbers))  # შედეგი: 6



#6. list() 

#დანიშნულება: სხვადასხვა მონაცემთა სტრუქტურის შექმნა.
#მაგალითი:


print(list("abc"))  # შედეგი: ['a', 'b', 'c']



#5)(***BOSS LEVEL***) მომხმარებელს შემოატანინეთ მისი გვარი, შემდეგ შეეკითხეთ უნდა თუ არა რომ მისი გვარი გადაიყვანოს დიდ ასოებად, 
# თუ გიპასუხათ "yes" მაშინ დაუბეჭდეთ მისი სახელი დიდი ასოებით, თუ გიპასუხათ "no" დაუბეჭდეთ უბრალოდ მისი სახელი. (მინიშნება: გაკვეთილის 
# ბოლოს განვიხილეთ ზედაპირულად)
 

 # მომხმარებლისგან გვარის შეყვანა
surname = input("შეიყვანეთ თქვენი გვარი: ")

# მომხმარებელს ვეკითხებით, უნდა თუ არა გვარის დიდ ასოებად გადაყვანა
answer = input("გინდათ, რომ თქვენი გვარი გადაიყვანოთ დიდ ასოებად? (yes ან no): ")

# ვამოწმებთ პასუხს და შესაბამის შედეგს ვბეჭდავთ
if answer == "yes":
    print("თქვენი გვარი დიდი ასოებით:", surname.upper())
elif answer == "no":
    print("თქვენი გვარი:", surname)
else:
    print("გთხოვთ, უპასუხეთ მხოლოდ 'yes' ან 'no'.")








