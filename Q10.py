def luhn_check(card_number):
    card_number = str(card_number)
    total = 0
    reverse = card_number[::-1]
    for i in range(len(reverse)):
        digit = int(reverse[i])
        if i % 2 == 1:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        total += digit
    return total % 10 == 0
card = input("Enter credit card number: ")
if luhn_check(card):
    print("Valid credit card number")
else:
    print("Invalid credit card number")