#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:] # Exclude the script name from the argument list 
    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    for index, arg in enumerate(argv, start=1):
        print("{}: {}".format(index, arg))
