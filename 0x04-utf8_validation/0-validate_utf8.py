#!/usr/bin/python3
"""ALx Interview Questions
   UTF-8 Validation module
"""


def encoding_bytes(value: int) -> int:
    """Determines the number of bytes used to encode a character
       based on the first byte value @value

       Args:
         value: an integer representing the value of the first byte
                of  a chain of chars

       Returns:
         the number of bytes used to encode the char accoring to UTF-8
         encoding standard
         returns -1 if invalid
    """
    if value & int('10000000', 2) == 0:
        return 1
    elif value & int('11100000', 2) == int('11000000', 2):
        return 2
    elif value & int('11110000', 2) == int('11100000', 2):
        return 3
    elif value & int('11111000', 2) == int('11110000', 2):
        return 4
    else:
        return -1


def validUTF8(data):
    """Checks if a given data set represents a valid UTF-8 encoding"""
    i = 0
    while i < len(data):
        if data[i] > 255 or data[i] < 0:
            return False

        skip = encoding_bytes(data[i])
        if skip == -1:
            return False
        for j in range(1, skip):
            if (
                i + j >= len(data) or 
                data[i + j] & int('11000000', 2) != int('10000000', 2)
            ):
                return False

        i += skip
    return True
