#! /usr/bin/env python3


'''
Project 1 - Bagles
11 August, 2023
'''


import random


def main():
    number = str(random.randint(0, 999)).rjust(3, '0')

    print("Bagels, a deductive logic game.")
    print("I am thinking of a 3-digit number. Try to guess what it is.")
    print("Here are some clues:")
    print("When I say:\tThat means:")
    print("  Pico\t\tOne digit is correct but in the wrong position.")
    print("  Fermi\t\tOne digit is correct and in the right position.")
    print("  Bagels\tNo digit is correct.")
    print("I have thought up a number.")
    print("You have 10 guesses to get it.")

    for _ in range(10):
        guess = input(f"Guess #{_}: ")

        if not guess.isnumeric() or (len(guess) != 3):
            print("Invalid guess!!!")
            continue

        if guess == number:
            print("You got it!")
            return

        no_match = True
        for index in range(3):
            if guess[index] in number:
                no_match = False
                if guess[index] == number[index]:
                    print("Fermi", end=" ")
                else:
                    print("Pico", end=" ")

        if no_match:
            print("Bagels", end=" ")

        print()


if __name__ == '__main__':
    main()
