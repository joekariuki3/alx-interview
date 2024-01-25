#!/usr/bin/python3
"""script that reads from stdin
and parses log files"""

import sys
import re


def readStdIn():

    count = 10
    increment = 0
    totalSize = 0
    codes = {200: 0,
             301: 0,
             400: 0,
             401: 0,
             403: 0,
             404: 0,
             405: 0,
             500: 0}

    for line in sys.stdin:
        s = r'(\S+) - \[([^]]+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
        match = re.match(s, line)
        if match:
            """get relevant data from the line"""
            ip_address, date, status_code, file_size = match.groups()
            totalSize += int(file_size)

            """keep count"""
            increment += 1

            """count status codes of each line"""
            status_code = int(status_code)
            codes[status_code] += 1

            """if count is 10 print statistics"""
            if increment == count:
                """increment count by 10"""
                count += 10
                printStatistics(totalSize, codes)


def printStatistics(totalSize, codes):
    """prints out the statstics"""
    # print size
    print(f"File size: {totalSize}")

    # print codes
    for code, value in sorted(codes.items()):
        if value > 0:
            print(f"{code}: {value}")


if __name__ == "__main__":
    readStdIn()