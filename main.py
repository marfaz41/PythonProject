
unit = input("Is this temprature in celsius or fahremheight (C/F): ")
temp = float(input("Enter the temprature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temprature in fahremheight is: {temp}"f" ")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9)
    print(f"The temprature in celcius is: {temp}C")
else:
     print(f"{unit} is an invalid unit of measurement")
