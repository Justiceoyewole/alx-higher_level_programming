#!/usr/bin/python3
def print_last_digit(number):
    # Get the last digit by taking the absolute value and modulo 10
    last_digit = abs(number) % 10
    # Print the last digit
    print("{}".format(last_digit), end="")
    return last_digit
