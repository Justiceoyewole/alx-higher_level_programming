#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Retrieve arguments, excluding the script name
    argv = sys.argv[1:]

    # Convert each argument to an integer and calculate the sum
    total = sum(int(arg) for arg in argv)

    # Print the result of the addition
    print(total)
