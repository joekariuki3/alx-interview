#!/usr/bin/python3
"""UTF-8 Validation"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """check the int values in the list
    if they satisfy the rules of a sequence of utf-8
    encoding retuen True else return False"""

    index = 0
    data_length = len(data)

    while index < data_length:
        byte = data[index]  # current byte

        if byte < 128:  # Ascii 0 to 127 valid utf-8
            index += 1  # Move to the next byte
        # Two-byte sequence 192-223 (110xxxxx 10xxxxxx)
        elif 192 <= byte <= 223:
            # Check if there are enough bytes left in the data
            # list and if the next byte starts with '10'
            if index + 1 >= data_length or not (128 <= data[index + 1] < 192):
                return False
            # Move to the next character after the two-byte sequence
            index += 2
        # Three-byte sequence 224-239 (1110xxxx 10xxxxxx 10xxxxxx)
        elif 224 <= byte <= 239:
            # Check if there are enough bytes left
            # in the data list and if the next two bytes start with '10'
            if (index + 2 >= data_length or not
                    (128 <= data[index + 1] < 192 and
                        128 <= data[index + 2] < 192)):
                return False
            index += 3  # move next to three-byte
        # Four-byte sequence 240-247 (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
        elif 240 <= byte <= 247:
            # Check if there are enough bytes left in the data list and
            # if the next three bytes start with '10'
            if (index + 3 >= data_length or
                    not (128 <= data[index + 1] < 192
                         and 128 <= data[index + 2] < 192
                         and 128 <= data[index + 3] < 192)):
                return False
            index += 4  # Move to next four-byte sequence
        else:
            return False  # no valid UTF-8 sequence range found

    return True  # If all bytes are valid UTF-8 sequences, return True
