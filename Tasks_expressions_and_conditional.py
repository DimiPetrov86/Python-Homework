# logical_expressions_and_conditional_statements_tasks.py

# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that takes a number as input and checks if it is positive, negative, or zero.
"""

### Your code here
x = float(input('Enter a number: '))
if x>0:
    print('Number', x, 'is positive.')
elif x==0:
    print('Number', x, 'is zero.')
elif x==-273:
    print('Number is absolute zero')
else:
    print('Number', x, 'is negative.')
### EXPECTED OUTPUT:
# "Enter a number: -2.45"
# "Number -2.45 is negative."


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a program to check whether a year input by the user is a leap year or not. Use the rule for Gregorian calendar:
    Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.
    For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.
"""

### Your code here
year = int(input('Enter an year: '))
if year % 400 == 0:
    print(f'{year} is a leap year.')
elif year % 100 == 0:
    print(f'{year} is not a leap year')
elif year % 4 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
### EXPECTED OUTPUT:
# Enter a year: 2024
# 2024 is a leap year

# Enter a year: 2050
# 2050 is not leap year.


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Develop a simple temperature converter program that converts temperatures from Fahrenheit to Celsius and vice versa based on user choice. Make a user-friendly interface as given in EXPECTED OUTPUT:.

    Temperature conversions use the following formulas:
    Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32.
    Temperature in degrees Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9.
"""

### Your code here
Head='Fahrenheit/Celsius Converter'
width=50
print(f'#{Head:*^{width}}#')
print(f'#{" 1 => Convert to Fahrenheit":<{width}}#')
print(f'#{" 2 => Convert to Celsius":<{width}}#')
print(f'*{"*":*^{width}}*')      
chosen_unit = int(input('Enter Your choice [1/2]:'))
if chosen_unit == 1:
    unit_value = float(input('Enter temperature in C '))
elif chosen_unit == 2:
    unit_value = float(input('Enter temperature in F '))
if chosen_unit == 1:
    print(f"{unit_value}C = {unit_value *9/5+32}F")
elif chosen_unit == 2:
    print (f"{unit_value}F = {(unit_value-32)*5/9}C")
### EXPECTED OUTPUT:
# **********Fahrenheit/Celsius Converter ***********
# # 1 => Convert to Fahrenheit                     #
# # 2 => Convert to Celsius                        #
# **************************************************
# Enter your choice [1/2]: 1
# Enter temperature in C: 20
# 20.0C = 68.0F


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    Write a Body mass index (BMI) calculator program, which asks the user for:
    weight in kilograms
    height in meters

    Calculate the BMI = W / (H*H)
    where:
    W = weight in kilograms
    H = height in meters

    Display to the user the BMI and basic category, using next table:

    | ------------------------------- | ----------- |
    | category                        | BMI         |
    | ------------------------------- | ----------- |
    | Underweight (Severe thinness)   | < 16.0      |
    | Underweight (Moderate thinness) | 16.0 - 16.9 |
    | Underweight (Mild thinness)     | 17.0 - 18.4 |
    | Normal range                    | 18.5 - 24.9 |
    | Overweight (Pre-obese)          | 25.0 - 29.9 |
    | Obese (Class I)                 | 30.0 - 34.9 |
    | Obese (Class II)                | 35.0 - 39.9 |
    | Obese (Class III)               | ≥ 40.0      |
    | ------------------------------- | ----------- |
"""

### Your code here
chosen_unit = int(input("Select type of measures "))
if chosen_unit == 1:
    weight_kg = float(input("Enter Your weight in kilograms " ))
    height_m = float(input("Enter Your height in meters "))
    bmi = float(f'{round(weight_kg / (height_m*height_m), 2)}')
elif chosen_unit == 2:
    weight_lbs = float(input("Enter Your weight in pounds "))
    height_ft = float(input("Enter Your height in feet "))
    height_in = float(input("Enter inches "))
    height_total = float(f'{height_ft*12+height_in}')
    bmi = float(f'{round(((weight_lbs*703) / height_total) / height_total, 2)}')
if bmi <16.0:
    cat = "Underweight (Severe thinness)"
elif 16.0 <= bmi <= 16.9:
    cat = "Underweight (Moderate thinness)"
elif 17.0 <= bmi <= 18.4:
    cat = "Underweight (Mild thinness)"
elif 18.5 <= bmi <= 24.9:
    cat = "Normal Range"
elif 25.0 <= bmi <= 29.9:
    cat = "Overweight (Pre-obese)"
elif 30.0 <= bmi <= 34.9:
    cat = "Obese (Class I)"
elif 35.0 <= bmi <= 39.9:
    cat = "Obese (Calss II)"
else:
    cat = "Obese (Class III)"
print('Your BMI =',  bmi, 'Category:', cat)
### EXPECTED OUTPUT:
# Enter weight in kilograms: 92
# Enter height in meters: 1.78
# Your BMI = 29.04, Category: Overweight (Pre-obese)