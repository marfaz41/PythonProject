#num = 5
#a = 6
#b = 7
#age = 13
#temprature = 12
#user_role = "admin"

#print("Positive" if num > 0 else "Negtive")
#result = "EVEN" if num / 2 == 0 else "ODD"
#max_num = a if a > b else b
#min_num = a if a < b else b
#status = "Teenagers" if age >= 17 else "child"
#weather = "HOT" if temprature > 20 else "COLD"
#access_level = "Full Access" if user_role == "admin" else "Limited Access"
#print(access_level)

#name = input("Enter your full name: ")
#phone_num = input("Enter your phone #: ")


#result = len(name)
#result = name.find("A")
#result = name.rfind("A")
#name = name.capitalize()
#name = name.lower()
#name = name.isdigit()
#result = name.isalpha()
#result = phone_num.count
#phone_number = phone_number.replace("-", "")
#print(phone_number)

#username = input("Enter a username! ")

#if len(username) > 12:
#   print("Your username can`t be more than 12 characters")
#elif not username.find(" ") == -1:
  #print("Your username can`t contain spaces")
#elif not username.isalpha():
    #print("Your username cant contain numbers")

#print("Your username can`t contain spaces")
#print("Welcome {username) ")


#credit_number = "1234-5678-9012-3456"

#print(credit_number[6])
#print(credit_number[0:4])
#print(credit_number[5:9])
#print(credit_number[5:])
#print(credit_number[-6])
#print(credit_number[::3])

#credit_number = (credit_number[::-1])
#print(credit_number)

#price1 = 3000.14159
#price2 = -98700.65
#price3 = 1200.34

#print(f"price 1 is #{price1:,.2f}")
#print(f"price 2 is #{price2:,.2f}")
#print(f"price 3 is #{price3:,.2f}")


#num = int(input("Enter a # between 1 - 10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))
    print(f"your number is {num} ")


#import turtle

#screen = turtle.Screen()
#screen.bgcolor("black")
#pen = turtle.Turtle()
#pen.speed(0)
#pen.pensize(3)

#colors = ["red", "cyan", "lime", "blue", "orange"]

#for i in range(180):
    #pen.pencolor(colors[i % len(colors)])
    #pen.forward(i * 2)
    #pen.right(69)

#turtle.done()

