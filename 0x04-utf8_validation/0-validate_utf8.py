#!/usr/bin/python3
"""validate UTF-8"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    validList = []
    for index, bit in enumerate(data):
        bit = bin(bit).replace("0b", "")
        # has more less than 8 bit meading starts
        # with 0 it is ASCII valid unicode
        if len(bit) <= 7:
            validList.append(1)
        elif len(bit) > 7:
            # more than 7 bit meaning unicode lets check
            # 2 bytes start with 110 next 2 bytes start with 10
            if bit[0] == 1 and bit[1] == 1 and bit[2] == 0:
                # check next 2 bytes
                for i in range(1, 3):
                    if data[index + i][0] == 1 and data[index + i][1] == 0:
                        validList.append(1)
                    else:
                        validList.append(0)

            # 3 bytes start with 1110 next 3 bytes start with 10
            elif bit[0] == 1 and bit[1] == 1 and bit[2] == 1 and bit[3] == 0:
                # check next 3 bytes
                for i in range(1, 4):
                    if data[index + i][0] == 1 and data[index + i][1] == 0:
                        validList.append(1)
                    else:
                        validList.append(0)

            # 4 bytes start with 11110 next 4 bytes start wit 10
            elif (bit[0] == 1 and bit[1] == 1 and bit[2] == 1
                    and bit[3] == 1 and bit[4] == 0):
                # check next 2 bytes
                for i in range(1, 5):
                    if data[index + i][0] == 1 and data[index + i][1] == 0:
                        validList.append(1)
                    else:
                        validList.append(0)
    if 0 in validList or not validList or not len(data) == len(validList):
        return False
    return True
