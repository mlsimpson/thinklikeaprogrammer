# • Read character by character until we reach an end-of-line.
#
# • Convert a series of characters representing a number to an integer.
#
# • Convert an integer 1–26 into an uppercase letter.
#
# • Convert an integer 1–26 into a lowercase letter.
#
# • Convert an integer 1–8 into a punctuation symbol based on Table 2-3.
#
# • Track a decoding mode.

import string

# Creates a number by entering one character (digit) at a time
def num_by_char():
    x = input()

    if x != 'q' and x != ',':
        num = int(x)
        x = input()
        while x != 'q' and x != ',':
            num = (num * 10) + int(x)
            x = input()

        # when a comma ',' is entered,
        # we have reached the end of our num
        if x == ',':
            return num
        if x == 'q':
            return 'quit'
    else:
        return 'quit'

def decode_message():
    intro = """Enter numerical characters one by one. End the current number with a single
comma ',' on a line. End every full number with the comma. Quit with 'q'
after all numbers and comma separators have been entered."""
    print(intro)

    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    punct = ['!', '?', ',', '.', ' ', ';', '"', '\'']
    mode = "upper"
    message = ""
    done = False

    while not done:
        x = num_by_char()

        if x == "quit":
            done = True
        else:
            if mode == 'upper':
                res = (x % 27)
                if res == 0:
                    mode = 'lower'
                    continue
                message += upper[res - 1]
            if mode == 'lower':
                res = (x % 27)
                if res == 0:
                    mode = 'punct'
                    continue
                message += lower[res - 1]
            if mode == 'punct':
                res = (x % 9)
                if res == 0:
                    mode = 'upper'
                    continue
                message += punct[res - 1]

    print(message)
    return message

decode_message()

