#Define a function named “triple_and” that takes three parameters andreturns True only if all three are True; otherwise, return False.
def triple_and(a, b, c):
    return bool(a and b and c)
a = input("Value of a: ")
b = input("Value of b: ")
c = input("Value of c: ")
a = (a == "true")
b = (b == "true")
c = (c == "true")

print("Result:", triple_and(a, b, c))
