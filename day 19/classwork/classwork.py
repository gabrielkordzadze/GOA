#1)შექმენით სია შემდგარი 10 ელემენტისგან, და გამოიტანეთ მხოლოდ კენტ ინდექსზე მდგომი ელემენტი
names = ["gabo","luka","saba","misho","vano","gia","gio","lile",]
for i in range(10):
    if i % 2 == 1:
        print(names[i])

#2)შექმენით სია რომელიც შედგება 5 რიცხვისგან, გადაუარეთ ამ სიას for ციკლით და შეაჯამეთ თითოეული რიცხვი, ბოლოს გამოიტანეთ ამ რიცხვების ჯამი (დაგჭირდებათ ერთი დამატებითი დამთვლელი ცვლადი (ჯამის ცვლადი, რომელსაც თითოეული რიცხვი დაემატება ყოველ იტერაციაზე))


number = [1,2,3,4,5]
counter = 0
for i in number:
    counter = counter + i
print(counter)
    


#3)შექმენით სია შემდგარი 10 რიცხვისგან, გადაურეთ for ციკლით, შეამოწმეთ კენტია თუ ლუწი, თუ ლუწია დაბეჭდეთ i, "luwia", თუ კენტია i, "kentia"
  
numbers = [1,2,4,5,6,7,8,9,10]

for i in numbers:
    if i % 2 == 0:
        print(i,"luwia")

    else:
        print(i,"kentia")
