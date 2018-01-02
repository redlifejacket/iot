#!/usr/bin/python3
# Shyam Govardhan
# 3 December 2018
# Coursera: The Raspberry Pi Platform and Python Programming for the Raspberry Pi
# Module 3 Assignment

numlist = []
SENTINEL_VALUE = "end"
PROMPT_MESSAGE = "Enter a number (type [" + SENTINEL_VALUE + "] to initiate sort): "
ERROR_MESSAGE = ": is not a numeric value, please try again"

# User input validation
def enterNumber(promptMessage, sentinelValue, errorMessage):
    while True:
        try:
            sval = input(promptMessage)
            if (sval == sentinelValue):
                return sentinelValue
                break
            ival = int(sval)
        except ValueError:
            print(sval + errorMessage + "\n")
            continue
        else:
           return ival
           break

# Main Program: Read input until user enters the SENTINEL_VALUE
while True:
    val = enterNumber(PROMPT_MESSAGE, SENTINEL_VALUE, ERROR_MESSAGE)
    if (val == SENTINEL_VALUE):
        break
    numlist.append(val)

numlist.sort();

for idx in range(0, len(numlist)):
    print(numlist[idx], end='')
    if (idx < len(numlist) - 1):
        print(", ", end='')
