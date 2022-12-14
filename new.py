#!/usr/bin/env python3
"""Create a solution file."""
import argparse
import itertools
import os
import re

YEAR = 2022

def get_next_day(year):
    regex = re.compile(r"^\d{2}\.py$")
    days = sorted([int(f[0:2]) for f in os.listdir(str(year)) if regex.match(f)])
    for i in itertools.count(1):
        if i not in days:
            return i

def get_multiline(prompt):
    print(prompt)
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)

    return "\n".join(contents)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--day",  type=int, help="Advent of code day..")
    parser.add_argument("-y", "--year", type=int, help="Which year to run.")

    args = parser.parse_args()

    if args.year:
        year = args.year
    else:
        year_input = input(f"year (default={YEAR}): ")
        year = int(year_input) if year_input else YEAR

    if args.day:
        day = args.day
    else:
        next_day = get_next_day(year)
        day_input = input(f"day (default={next_day}): ")
        day = int(day_input) if day_input else next_day

    test_input = get_multiline("Enter test input. Ctrl-D or Ctrl-Z ( windows ) to save.")
    test_sol = input("Enter test solution: ")
    full_input = get_multiline("Enter full input. Ctrl-D or Ctrl-Z ( windows ) to save.")

    print(f"year: {year}, day: {day}")
    filename = f"{year}/{day:02}.py"
    print(filename)
    assert not os.path.exists(filename)
    f = open(filename, "w")

    f.write("def part1(ll):\n")
    f.write("    raise NotImplementedError\n")
    f.write("\n")
    f.write("def part2(ll):\n")
    f.write("    raise NotImplementedError\n")
    f.write("\n")
    f.write(f'TEST_INPUT = """{test_input}"""\n')
    f.write("\n")
    f.write(f"TEST_SOL = [{test_sol}]\n")
    f.write("\n")
    f.write(f'FULL_INPUT = """{full_input}"""\n')
    f.write("\n")
    f.write("FULL_SOL = []")

if __name__ == "__main__":
    main()
