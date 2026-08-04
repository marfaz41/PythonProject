# python weight converter

weight = float(input("Enter your weight"))
unit = input("Kilograms or pounds? (K or L): ")

if unit =="K":
     weight = weight * 2.205
     unit == "lbs."
     print(F"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L":
     weight = weight / 2.205
     unit == "kgs."
     print(F"Your weight is: {round(weight, 1)} {unit}")

else:
     print(F"{unit} was not valid")

