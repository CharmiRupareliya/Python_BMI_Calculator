import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)  # Initializing colorama to automatically reset color settings

name = input(Fore.MAGENTA + "Enter your Name: ")
print()
weight = float(input(Fore.CYAN + "Enter your weight in kilogram :"))
feet = float(input(Fore.CYAN + "Enter your height in feet :"))

height = feet * 0.3048  # Converting height from feet to meters (1 foot = 0.3048 meters)
BMI = (weight) / (height * height)  # Calculating BMI (Body Mass Index) using the formula
print(Fore.BLUE + "Your BMI is :",BMI)

# Checking BMI value to categorize weight status
if BMI > 0:
    if (BMI < 18.5) :
            print(Fore.LIGHTBLUE_EX +  f"{name}, You are Underweight.")
    elif (BMI >= 18.5 and BMI < 24.9) :
            print(Fore.LIGHTBLUE_EX + f"{name}, You are Normal weight.")
    elif (BMI >=24.9 and BMI < 29.9):
             print(Fore.LIGHTBLUE_EX +  f"{name}You are Overweight.")
    else:
        # If BMI is 29.9 or higher, additional categories can be added as needed
        print(Fore.LIGHTMAGENTA_EX +  f"{name}, You are Obese.")
else:
    print(Fore.RED + "Enter valid inputs...")






