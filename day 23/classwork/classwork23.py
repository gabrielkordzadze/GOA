#1)კომენტარის მეშვეობით ახსენით .lower() / .upper() / .capitalize() / .find() ფუნქციების დანიშნულება

# .Lower() აბრუნებს სტრიქონს სადაც ყველა ასო დაპატარავებულია

# .upper() აბრუნებს სტრიქონს სადაც ყველა ასო გადიდებულია

# .capitalize()  აბრუნებს სტრიქონს სადაც პირველი ასო გადაყვანილია დიდ ასოდ და დანარჩენი პატარა ასოებად

# .find() ეძებს სტრიქონში სიმბოლოს ან სიტყვას და აბრუნებს მის ინდექსს



#2)მომხმარებელს შემოატანინეთ მისი გვარი და შეამოწმეთ, თუ გვარის პირველი ასო არის დიდი ასო, მაშინ დაუბეჭდეთ
#  "Hello", თუ არ არის მაშინ დაუბეჭდეთ "Bye


surname = input("enter your surname: ")
if surname[0]==surname[0].upper():
    print("Hello")
    

else:
    print("Bye")



#3)მომხმარებელს შემოატანინეთ სახელი, შემდეგ შემოატანინეთ ასო და თუ ამ სახელში ეს ასო არიქნება, მაშინ გამოუტანეთ
#  "Can't find character", თუ იქნება მაშინ გამოუტანეთ "found it" და გვერდზე მიუწერეთ ამ ასოს ინდექსი



name = input("Enter your name: ") 
char = input("Enter a character to search for: ") 

if char in name: 
    print(f"Found it at index {name.find(char)}")  
else:
    print("Can't find character")



#4)მომხმარებელს შემოატანინეთ მისი გვარი, შემდეგ შეეკითხეთ როგორ უნდა რო შეიცვალოს მისი გვარის ასოები, თუ გიპასუხებთ "upper" გადაიყვანეთ მთლიანი
#  გვარი დიდ ასოებად, თუ გიპასუხებთ "lower" გადაიყვანეთ მთლიანი გვარი პატარა ასოებად და თუ გიპასუხებთ "capitalize" გადაიყვანეთ გვარის მხოლოდ 
# პირველი ასო დიდ ასოდ.
 



surname = input("Enter your surname: ")  
choice = input("How would you like to change your surname (upper/lower/capitalize)? ").lower()

if choice == "upper":
    print(surname.upper())  
elif choice == "lower":
    print(surname.lower())  
elif choice == "capitalize":
    print(surname.capitalize())  
else:
    print("Invalid choice")  