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
    for space in range(row - 1):
        message += ' '
    for hash in range(8 - 2 * (row - 1)):
        message += '#'
    print(message)

