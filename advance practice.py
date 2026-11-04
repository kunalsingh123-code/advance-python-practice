

# Question 1: Find the data type of every value in a mixed list.

a = [10, 10.5, "Python", True]

for i in a:
    print(i, type(i))
# ============================================================

# Question 2: Convert a nested list into a tuple of tuples.

a = [[1, 2], [3, 4], [5, 6]]

b = tuple(tuple(i) for i in a)

print(b)
# ============================================================

# Question 3: Remove duplicate values from a mixed list without changing order.

a = [10, "Python", 20, 10, "Java", 20, "Python"]
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)
# ============================================================

# Question 4: Check whether a number is a power of 2.

n = int(input("Enter a number: "))

if n > 0 and (n & (n - 1)) == 0:
    print("Power of 2")
else:
    print("Not a power of 2")
# ============================================================

# Question 5: Swap two numbers using bitwise XOR.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:", a, b)
# ============================================================

# Question 6: Check whether a number is divisible by both 4 and 6.

n = int(input("Enter a number: "))

if n % 4 == 0 and n % 6 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")
# ============================================================

# Question 7: Calculate electricity bill using different unit rates.
# First 100 units = Rs. 2, next 100 = Rs. 3, above 200 = Rs. 5.

u = int(input("Enter units: "))

if u <= 100:
    bill = u * 2
elif u <= 200:
    bill = 100 * 2 + (u - 100) * 3
else:
    bill = 100 * 2 + 100 * 3 + (u - 200) * 5

print("Total bill:", bill)
# ============================================================

# Question 8: Check whether three sides can form a triangle.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")
# ============================================================

# Question 9: Find the type of triangle.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
# ============================================================

# Question 10: Create a simple ATM menu.

balance = 5000

while True:
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Balance")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        amt = int(input("Enter amount: "))
        if amt <= balance and amt > 0:
            balance = balance - amt
            print("Withdraw successful")
        else:
            print("Insufficient balance")
    elif ch == 2:
        amt = int(input("Enter amount: "))
        balance = balance + amt
        print("Deposit successful")
    elif ch == 3:
        print("Balance:", balance)
    elif ch == 4:
        break
    else:
        print("Wrong choice")
# ============================================================

# Question 11: Calculate income tax using different tax slabs.
# These are assumed rates for this practical.

income = float(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = 12500 + (income - 500000) * 0.20
else:
    tax = 112500 + (income - 1000000) * 0.30

print("Income tax:", tax)
# ============================================================

# Question 12: Create a simple calculator using if-elif.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

ch = int(input("Enter choice: "))

if ch == 1:
    print("Answer:", a + b)
elif ch == 2:
    print("Answer:", a - b)
elif ch == 3:
    print("Answer:", a * b)
elif ch == 4:
    if b != 0:
        print("Answer:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")
# ============================================================

# Question 13: Print all prime numbers between 1 and n.

n = int(input("Enter n: "))

for num in range(2, n + 1):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        print(num, end=" ")
# ============================================================

# Question 14: Find factorial of a number using a loop.

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial:", fact)
# ============================================================

# Question 15: Print Fibonacci series up to n terms.

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
# ============================================================

# Question 16: Check whether a number is an Armstrong number.

n = int(input("Enter a number: "))
temp = n
total = 0
power = len(str(n))

while temp > 0:
    digit = temp % 10
    total = total + digit ** power
    temp = temp // 10

if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
# ============================================================

# Question 17: Reverse a number and check whether it is palindrome.

n = int(input("Enter a number: "))
temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

print("Reverse:", rev)

if n == rev:
    print("Palindrome")
else:
    print("Not palindrome")
# ============================================================

# Question 18: Find GCD of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    r = a % b
    a = b
    b = r

print("GCD:", abs(a))
# ============================================================

# Question 19: Write a function to check whether a string is palindrome.

def check(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")

s = input("Enter a string: ")
check(s)
# ============================================================

# Question 20: Count vowels and consonants in a string using a function.

def count(s):
    v = 0
    c = 0
    for i in s.lower():
        if i.isalpha():
            if i in "aeiou":
                v = v + 1
            else:
                c = c + 1
    print("Vowels:", v)
    print("Consonants:", c)

s = input("Enter a string: ")
count(s)
# ============================================================

# Question 21: Calculate simple interest and compound interest using a function.

def interest(p, r, t):
    si = (p * r * t) / 100
    ci = p * (1 + r / 100) ** t - p
    print("Simple interest:", si)
    print("Compound interest:", round(ci, 2))

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
interest(p, r, t)
# ============================================================

# Question 22: Return all factors of a number using a function.

def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

n = int(input("Enter a number: "))
factors(n)
# ============================================================

# Question 23: Find second largest number in a list using a function.

def second_largest(a):
    a = list(set(a))
    a.sort()
    if len(a) >= 2:
        print("Second largest:", a[-2])
    else:
        print("Second largest does not exist")

a = [10, 20, 30, 40, 40, 50]
second_largest(a)
# ============================================================

# Question 24: Merge two lists without duplicate values.

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = a.copy()

for i in b:
    if i not in c:
        c.append(i)

print(c)
# ============================================================

# Question 25: Find second largest and second smallest elements.

a = [10, 20, 30, 40, 50]
a = sorted(set(a))

if len(a) >= 2:
    print("Second largest:", a[-2])
    print("Second smallest:", a[1])
else:
    print("Not possible")
# ============================================================

# Question 26: Rotate a list to the left by k positions.

a = [1, 2, 3, 4, 5]
k = int(input("Enter k: "))

k = k % len(a)
a = a[k:] + a[:k]

print(a)
# ============================================================

# Question 27: Separate even and odd numbers into two lists.

a = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)
# ============================================================

# Question 28: Find common elements between two lists.

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
c = []

for i in a:
    if i in b and i not in c:
        c.append(i)

print("Common elements:", c)
# ============================================================

# Question 29: Count frequency of each element in a tuple.

a = (1, 2, 3, 2, 1, 4, 2, 3)

for i in set(a):
    print(i, ":", a.count(i))
# ============================================================

# Question 30: Find union, intersection and difference of two sets.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
# ============================================================

# Question 31: Check whether one set is a subset of another.

a = {1, 2}
b = {1, 2, 3, 4}

if a.issubset(b):
    print("A is subset of B")
else:
    print("A is not subset of B")
# ============================================================

# Question 32: Count frequency of words in a sentence.

s = input("Enter a sentence: ")
words = s.lower().split()
d = {}

for i in words:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print(d)
# ============================================================

# Question 33: Create a dictionary from two lists.

keys = ["Name", "Age", "City"]
values = ["Kunal", 22, "Nashik"]

d = dict(zip(keys, values))
print(d)
# ============================================================

# Question 34: Sort a dictionary by its values.

d = {"Apple": 50, "Banana": 20, "Mango": 80, "Orange": 40}

x = dict(sorted(d.items(), key=lambda i: i[1]))
print(x)
# ============================================================

# Question 35: Read a text file and count lines, words and characters.
# Create sample.txt in the same folder before running.

f = open("sample.txt", "r")
data = f.read()
f.close()

lines = data.splitlines()
words = data.split()

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(data))
# ============================================================

# Question 36: Copy only even-numbered lines from one file to another.
# Create input.txt in the same folder before running.

f = open("input.txt", "r")
lines = f.readlines()
f.close()

f = open("output.txt", "w")

for i in range(len(lines)):
    if (i + 1) % 2 == 0:
        f.write(lines[i])

f.close()
print("Even lines copied")
# ============================================================

# Question 37: Handle invalid integer input using try-except.

try:
    n = int(input("Enter an integer: "))
    print("Number:", n)
except ValueError:
    print("Please enter a valid integer")
# ============================================================

# Question 38: Handle file not found error while reading a file.

try:
    f = open("sample.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File not found")
# ============================================================

# Question 39: Generate a random password using random and string modules.

import random
import string

n = int(input("Enter password length: "))
chars = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(n):
    password = password + random.choice(chars)

print("Password:", password)
# ============================================================

# Question 40: Find number of days between two dates using datetime module.

from datetime import datetime

d1 = input("Enter first date (DD-MM-YYYY): ")
d2 = input("Enter second date (DD-MM-YYYY): ")

date1 = datetime.strptime(d1, "%d-%m-%Y")
date2 = datetime.strptime(d2, "%d-%m-%Y")

days = abs((date2 - date1).days)
print("Number of days:", days)
