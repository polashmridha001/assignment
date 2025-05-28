# Number Pattern - Hollow Pyramid (for loop)
# Take an integer n and a symbol input and print a hollow pyramid pattern.
n = int(input("Enter height: "))
symbol = input("Enter symbol: ")

for i in range(1, n+1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(1, 2*i):
        if k == 1 or k == 2*i - 1 or i == n:
            print(symbol, end="")
        else:
            print(" ", end="")
    print()

#  Prime Number in a Range (for loop)
# # Take two integers a and b, and print all prime numbers between them. Use nested
# # loops and conditionals.
a= int(input("Enter start number"))
b= int(input("Enter end number "))

for number in range(a, b + 1):
    if number > 1:
        for i in range(2, number):

            if number % i ==0:
                break
        else:
            print(number)

# Number to Words Converter (while loop + conditionals)
# Input: a positive integer.
# Output: Print its digits as words (e.g., 123 → "One Two Three").
# Constraints: Use only conditionals (no string or list operations). You'll need to extract
# digits and print corresponding words.
number = int(input("Enter number:"))
reverse =0
while number> 0:
    reverse = reverse * 10 + number % 10
    number//=10
    while reverse>0:
        digit = reverse % 10
        reverse //= 10

        if digit==1:
            print("One", end=" ")

        elif digit==2:
            print("Two", end=" ")
        elif digit == 3:
            print("Three", end=" ")
        else:
            print("Invaild number ")

# Perfect Number Checker
# A number is perfect if the sum of its proper divisors (excluding itself) equals the
# number.
# Example: 28 → 1 + 2 + 4 + 7 + 14 = 28.
# Input a number and check if it's perfect.
number1 = int(input("Enter number:"))

sum_div = 0
for i in range(1, number1):
    if number1 % i ==0:
        sum_div +=i
if sum_div== number1:
    print("Perfect Number")
else:
    print("Not Perfect")

# Digital Root Calculator
# Take a number as input. Continuously sum its digits until only one digit remains.
# Example: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2.

num = int(input("Enter number: "))

while num > 9:
    sum_d = 0
    while num > 0:
        sum_d += num % 10
        num //= 10
    num = sum_d

print("Digital Root:", num)

# Binary to Decimal Converter (while loop)
# Input: A binary number (e.g., 1101).
# Output: Convert it to decimal using only math and conditionals (no built-in
# conversion).

binary = int(input("Enter binary number: "))
decimal = 0
base = 1

while binary > 0:
    last_digit = binary % 10
    decimal += last_digit * base
    base *= 2
    binary //= 10

print("Decimal:", decimal)

# Frequency of Each Digit (while loop + conditionals)
# Input: A number like 1223334444.
# Output: Count and print how many times each digit (0–9) appears.
# Restriction: Do not use strings or dictionaries. Use conditionals only.
num = int(input("Enter number: "))
c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = 0

while num > 0:
    d = num % 10
    num //= 10
    if d == 0: c0 += 1
    elif d == 1: c1 += 1
    elif d == 2: c2 += 1
    elif d == 3: c3 += 1
    elif d == 4: c4 += 1
    elif d == 5: c5 += 1
    elif d == 6: c6 += 1
    elif d == 7: c7 += 1
    elif d == 8: c8 += 1
    elif d == 9: c9 += 1


print("0:", c0)
print("1:", c1)
print("2:", c2)
print("3:", c3)
print("4:", c4)
print("5:", c5)
print("6:", c6)
print("7:", c7)
print("8:", c8)
print("9:", c9)
