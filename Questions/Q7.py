#Write a program to print the Fibonacci sequence up to n values, where n isprovided by the user.
n = int(input("Enter n: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    
    c = a + b
    a = b
    b = c
