# Largest among Three Numbers: Write a Python program that takes
# three numbers as input and prints out the largest among them.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))

if num1>num2 and num1>num3:
    print("Largest number", num1)

elif num2>num1 and num2>num3:
    print("Largest number", num2)

else:
    print("Largest number", num3)

# Quadrant Identifier: Write a Python program that takes the coordinates (x, y)
# of a point as input and prints out which quadrant it belongs to (1st, 2nd, 3rd, or
# 4th).
x = int(input("Enter Quadrants:"))
y = int(input("Enter Quadrants:"))

if x> 0 and y> 0:
    print("1st Quadrant")

elif x<0 and y>0:
    print("2nd Quadrant")
elif x<0 and y<0:
    print("3rd Quadrant")
elif x>0 and y<0:
    print("4th Quadrant")
elif x==0 and y==0:
    print("Orginal")

else:
    print("Axis")

# Age Classifier: Write a Python program that takes a person's age as input and
# prints out whether they are an infant (0-1), toddler (2-3), child (4-12), teenager
# (13-19), adult (20+).
age = int(input("Enter age:"))

if age>=0 and age<=1:
    print("Infant")

elif age<=3:
    print("Toddler")
elif age<=12:
    print("Child")
elif age<=19:
    print("Teenager")

else:
    print("Adult")

# BMI Calculator: Write a Python program that takes a person's height (in
# meters) and weight (in kilograms) as input and calculates their Body Mass
# Index (BMI). Print out their BMI and a message indicating whether they are
# underweight (<18.5), normal (18.5-24.9), overweight (25-29.9), or obese
# (>=30).
weight = float(input("Enter Weight (KG):"))
height = float(input("Enter Height (M):"))

bmi= weight/(height ** 2)

print("BMI:", bmi)

if bmi<18.5:
    print("Underweight")

elif bmi<25:
    print("Normal")
elif bmi<30:
    print("Overweight")

else:
    print("Obese")


# Temperature Converter: Write a Python program that takes a temperature
# input in Celsius and converts it to Fahrenheit if the temperature is above 0°C,
# or to Kelvin if the temperature is below 0°C.

temp = float(input("Enter temperature in Celsius:"))

fahrenheit = (temp * 9/5+ 32)  #Formula form wikipedia

if temp>0:
    print("Temperature in Fahrenheit:", fahrenheit,"°F")

else:
    kelvin = temp + 273.15
    print("Temperature in Kelvin:", kelvin)


# Simple Calculator: Input two numbers and an operator (+, -, *, /).Use
# if-elif to perform the operation and print the result. Handle division by zero
# using conditions.

a= float(input("Enter first number::"))
op= input("Enter operator (+, -, *, /):")
b= float(input("Enter second number:"))
# qurary= input("Enter queary (+, -, *, /):")

if op== '+':
    print("Result", a+b)
elif op== '-':
    print("Result", a-b)
elif op== '*':
    print("Result", a*b)
elif op== '/':
    if b !=0:
        print("Result", a/b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")


# FizzBuzz: Write a Python program that prints the numbers from 1 to 100. But for
# multiples of three, print "Fizz" instead of the number, and for the multiples of
# five, print "Buzz". For numbers that are multiples of both three and five, print
# "FizzBuzz" using a for loop.

for y in range(1,101):
    if y % 3 ==0 and y % 5 ==0:
        print("FizzBuzz")
    elif y%3==0:
        print("Fizz")
    elif y%5==0:
        print("Buzz")
    else:
        print(y)


# Sum of Digits: Write a Python program that takes an integer input from the
# user and calculates the sum of its digits using a while loop.
a = int(input("Enter number:"))
cnt=0

while a>0:
    a//=10
    cnt+=1
print("Sum of digits:",cnt)

# Print the pattern (for/while):1,22,333,4444,55555

for i in range(1, 6):
    print(str(i) * i)

# Password Retry System (while loop) : Predefined password. Let user try until
# correct or after 3 failed attempts show "Account locked"
passwd = "python"
attempts= 0

while attempts <3:
    user = input("Enter password:")
    if user == passwd:
        print("Access Granted")
        break
    else:
        print("Wrong password")
        attempts +=1

if attempts ==3:
    print("Account locked")

# Guess the Number Game (while loop): Consider a random number between 1
# and 10. Let user guess until correct. Give hints: “Too high” or “Too low”.

secret = 7
guess =0

while secret!=guess:
    guess= int(input("Enter number (1-10):"))
    if guess<secret:
        print("Too low")
    elif guess>secret:
        print("Too high")

    else:
        print("Correct")
