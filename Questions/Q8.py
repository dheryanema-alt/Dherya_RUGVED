#Write a Python program to divide a given string into equal parts of ncharacters (where n is provided by the user) that repeat the samesequence. Example: string = “abcdabcdabcdabcd”, n = 4 → output: “abcd”,“abcd”, “abcd”, “abcd”. If the division is not possible or the sequence is notthe same, print an appropriate error.#
a = input("Enter a string: ")
n = int(input("Enter number of characters in each part: "))
if len(a) % n != 0:
    print("Error: String cannot be divided into equal parts.")
else:
    parts = []

    for i in range(0, len(a), n):
        parts.append(a[i:i+n])

    if all(part == parts[0] for part in parts):
        print("Parts:", end=" ")
        for part in parts:
            print(part, end=" ")
    else:
        print("Error: The sequence is not the same.")
