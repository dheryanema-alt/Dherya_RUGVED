#Write a Python program to check whether a given number is a hill number.
n = input("Enter a number: ")
digits = [int(d) for d in n]
i = 1
while i < len(digits) and digits[i] > digits[i - 1]:
    i += 1
while i < len(digits) and digits[i] < digits[i - 1]:
    i += 1
if i == len(digits):
    print("Hill Number")
else:
    print("Not a Hill Number")
