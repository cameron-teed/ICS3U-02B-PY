#!usr/bin/env python

# Created by: Cameron Teed
# Created On: September 2019
# This program calculates the volume of a dodecahydron

import math
import constant


def main():
    # This program calculates the volume of a dodecahydron

    # Input
    lenght = int(input("enter the side lenght of your dodecahydron (cm): "))

    # Procces
    volume = constant.FORMULA*lenght**3

    # Output
    print("")
    print("volume is: {:,.6}cm³".format(volume))


if __name__ == "__main__":
    main()
