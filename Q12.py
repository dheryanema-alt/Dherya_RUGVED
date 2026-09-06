n = int(input("Enter n: "))

# Increasing part
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    
    for j in range(i):
        print("*", end=" ")
        
    print()

# Decreasing part
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    
    for j in range(i):
        print("*", end=" ")
        
    print()