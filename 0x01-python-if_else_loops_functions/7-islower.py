#!/usr/bin/python3
def islower(c):
    # Check if the character's Unicode code point is between 'a' and 'z'
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
