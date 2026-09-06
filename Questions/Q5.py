#Find the Fibonacci number for a given input using recursion.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter n: "))
print("Fibonacci number:", fibonacci(n))
