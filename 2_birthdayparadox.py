#! /usr/bin/env python3


import random


'''
Project 2 - Birthday Paradox
14 August, 2023
'''


MONTHS = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
)

DAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

SIMULATIONS = 100_000


def generate_random_birthday():
    index = random.randint(1, 12) - 1

    month = MONTHS[index]
    day = random.randint(1, DAYS[index])

    return f"{month} {day}"


def generate_birthday_list(count):
    birthdays = []
    for i in range(count):
        birthdays.append(generate_random_birthday())
    
    return birthdays


def check_birthday(birthdays):
    for bday in birthdays:
        if birthdays.count(bday) > 1:
            return bday
    
    return None


def main():
    print("How many birthdays shall i generate? (Max 100)")
    num = int(input(">"))

    print(f"Here are {num} birthdays:")

    birthdays = generate_birthday_list(num)
    print(*birthdays, sep=", ")

    if bday := check_birthday(birthdays):
        print(f"In this simulation, multiple people have a birthday on {bday}")
    else:
        print("In this situation, no one shares a birthday")
    
    print(f"Generating {num} random birthdays 100,000 times...")
    input("Press Enter to begin...")

    same = 0
    for i in range(SIMULATIONS):
        if i % 10_000 == 0:
            print(f"{i} simulations run...")
        
        birthdays = generate_birthday_list(num)
        if check_birthday(birthdays):
            same += 1
    print("100000 simulations run...")

    probablity = round(same / SIMULATIONS * 100, 2)
    print(f"Out of {SIMULATIONS} simulations of {num} people, there was a")
    print(f"matching birthday in that group {same} times. This means")
    print(f"that {num} people have a {probablity} % chances of")
    print(f"having a matching birthday in their group.")
    print(f"That's probably more than you think!")

    return 0


if __name__ == '__main__':
    main()