#!/usr/bin/env python3
# Created by: Shem
# Created on: 11/14/2025
# This program displays squares up to a positive number
# and then prints a cute smiling cat at the end.
counter = 0


def main():
    try:
        user_number = int(input("Enter a positive number: "))
        if user_number < 0:
            print("Enter a number above 0")
        # Display squares
        for counter in range(user_number + 1):
            power_of_two = counter**2
            print("{}^2 = {}".format(counter, power_of_two))
        print("Thank you for playing")
        print(" /\\_/\\  ")
        print("( ^_^ )")
        print(" > ^ < ")
    except ValueError:
        print("Invalid input! Please enter a valid positive integer.")


if __name__ == "__main__":
    main()
