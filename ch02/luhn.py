# Luhn Checksum from Think Like A Programmer
# ported to Python 3

# If the number already contains the check digit, drop that digit to form the
# "payload." The check digit is most often the last digit.
# With the payload, start from the rightmost digit. Moving left, double the
# value of every second digit (including the rightmost digit).
# Sum the digits of the resulting value in each position.
# Sum the resulting values from all positions repeatedly until a single digit,
# s remains (i.e. do Casting out nines on it).
# The check digit is calculated by 10 - (s % 10)

def double_digits(num):
    out = (num * 2)

    if out >= 10:
        return 1 + (out % 10)

    return out

# I made the logic of this a bit screwy to grok
def luhn():
    odd_len_checksum = 0
    even_len_checksum = 0

    # Don't actually need odd/even len checksum, just using this works
    checksum2 = 0

    position = 1

    print("Enter single digits one by one, pressing Enter after every entry.\n\
Press 'q' then Enter to quit.")
    x = input()

    while x != 'q':
        # We double even position digits from the right
        if position % 2 == 0:
            checksum2 += double_digits(int(x))
            odd_len_checksum += int(x)
            even_len_checksum += double_digits(int(x))
        else:
            checksum2 += int(x)
            odd_len_checksum += double_digits(int(x))
            even_len_checksum += int(x)

        position += 1

        x = input()

    if position % 2 == 0:
        checksum = even_len_checksum
    else:
        checksum = odd_len_checksum

    if checksum % 10 == 0:
        print("Valid checksum")
    else:
        print("Invalid checksum")

    print("checksum2 = ", checksum2)

    return checksum


