#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert lowercase to uppercase by subtracting 32
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
