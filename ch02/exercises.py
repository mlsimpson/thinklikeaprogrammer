# 2-1
# Using only single-character output statements that output a hash mark, a
# space, or an end-of-line, write a program that produces the following shape:
#
# ########
#  ######
#   ####
#    ##

for row in range(1, 5):
    message = ""
    for _ in range(row - 1):
        message += ' '
    for _ in range(8 - 2 * (row - 1)):
        message += '#'
    print(message)

print('\n')

# 2-2
# or how about:
#    ##
#   ####
#  ######
# ########
# ########
#  ######
#   ####
#    ##

# top half
for row in range(1, 5):
    message = ""
    for _ in range(abs(4 - row)):
        message += ' '
    for _ in range(2 * row):
        message += '#'
    print(message)

# bottom half
for row in range(1, 5):
    message = ""
    for _ in range(row - 1):
        message += ' '
    for _ in range(8 - 2 * (row - 1)):
        message += '#'
    print(message)

print('\n')

# 2-3
# Here’s an especially tricky one:
# #            #
#  ##        ##
#   ###    ###
#    ########
#    ########
#   ###    ###
#  ##        ##
# #            #

# top half
for row in range(1, 5):
    message = ""
    for _ in range(row - 1):
        message += ' '
    for _ in range(row):
        message += '#'
    for _ in range(4 * (4 - row)):
        message += ' '
    for _ in range(row):
        message += '#'
    print(message)

# bottom half
for row in range(1, 5):
    message = ""
    for _ in range(4 - row):
        message += ' '
    for _ in range(5 - row):
        message += '#'
    for _ in range(4 * (row - 1)):
        message += ' '
    for _ in range(5 - row):
        message += '#'
    print(message)

