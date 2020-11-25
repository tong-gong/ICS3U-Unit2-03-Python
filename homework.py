#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a program to calculate the circumference of a circle

import math


def main():
    radius = int(input("Enter the radius of the circle"))
    circumference = math.tau*radius
    print("")
    print("The perimeter is {}mm".format(circumference))


if __name__ == "__main__":
    main()
