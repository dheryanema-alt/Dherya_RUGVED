#Write a Python program to sort a string alphabetically and print the count of each character.
a=input("Enter The text: ")
sorted_char = sorted(a)
sorted_str = "".join(sorted_char)

print("Original text:", a)
print("Sorted character list:", sorted_char)
print("Rejoined sorted string:", sorted_str)   

print("\nCharacter counts:")
for k in sorted(set(a)):
    print(f"Count of '{k}': {a.count(k)}")

