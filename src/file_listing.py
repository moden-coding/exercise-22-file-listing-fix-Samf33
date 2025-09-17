#!/usr/bin/env python3

from calendar import day_abbr
from ctypes import sizeof
import re


def file_listing(filename="src/listing.txt"):
    dda = []
    with open(filename, "r") as f:
        for line in f:
            finding = re.findall(r'-all\s*(\d*)\s(.{3})\s*(\d*)\s(\d*):(\d*)\s(.*)', line)
            fixed = (int(finding[0][0]), finding[0][1], int(finding[0][2]), int(finding[0][3]), int(finding[0][4]), finding[0][5])
            print(fixed)
            dda.append(fixed)
    print(dda)
    return dda

def main():
    file_listing()

    #Begin tests
    #result = file_listing()
    #print(len(result))
    #Output should be: 47

    #for i in result:
    #   print(len(i))
    #Output should all be 6s as the length of each item is 6

    #for t in result:
    #   print(f"Items in result should be tuples and they are {type(t)}")
    #   print(f"First item in tuple should be an str, is {type(t[0])}")
    #   print(f"Second item in tuple should be an int, is {type(t[1])}")
    #   print(f"Third item in tuple should be an int, is {type(t[2])}")
    #   print(f"Fourth item in tuple should be an int, is {type(t[3])}")
    #   print(f"Fifth item in tuple should be an int, is {type(t[4])}")
    #   print(f"Sixth item in tuple should be an str, is {type(t[5])}")



if __name__ == "__main__":
    main()
