#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on March 2022
# This program calculates simple addition with inputs


def main():
    # this program calculates numbers inserted by user

    # input
    first_number = int(input("Enter the first number:"))
    second_number = int(input("Enter the second number:"))

    # process
    total = first_number + second_number

    # output
    print()
    print("{0} + {1} = {2}".format(first_number, second_number, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
