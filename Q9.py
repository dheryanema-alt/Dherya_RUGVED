#Write a Python function to encrypt a string using Caesar’s cipher.
def caesar_cipher(s, shift):
    result = ""
    for ch in s:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch
    return result
s = input("Enter a string: ")
shift = int(input("Enter shift: "))
print("Encrypted string:", caesar_cipher(s, shift))