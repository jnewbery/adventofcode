#!/usr/bin/env python3
"""Create a template solution file, and add input files and solutions to solutions.json."""
import argparse
from datetime import date
import itertools
import json
import os
from pathlib import Path
import shutil

def get_next_day(year):
    days = sorted([int(f.stem[4:6]) for f in Path("sols").glob('*') if f.name.startswith(f"{year}") and f.suffix == ".py"])
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

    parser.add_argument("-d", "--day",  type=int, help="Advent of code day.")
    parser.add_argument("-y", "--year", type=int, help="Which year to run.")

    args = parser.parse_args()

    if args.year:
        year = args.year
    else:
        this_year = date.today().year
        year_input = input(f"year (default={this_year}): ")
        year = int(year_input) if year_input else this_year

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
    puzzle_name = f"{year}{day:02}"
    filename = f"sols/{puzzle_name}.py"
    print(filename)
    assert not os.path.exists(filename)
    template_filename = "sols/template.py"
    shutil.copy(template_filename, filename)

    test_input_filename = f"sols/{puzzle_name}_test_input.txt"
    with open(test_input_filename, "w") as f:
        f.write(test_input)

    full_input_filename = f"sols/{puzzle_name}_input.txt"
    with open(full_input_filename, "w") as f:
        f.write(full_input)

    with open("sols/solutions.json", "r") as f:
        solutions = json.load(f)

    if puzzle_name not in solutions:
        solutions[puzzle_name] = {}
        solutions[puzzle_name]["1"] = {"test": test_sol}

    with open("sols/solutions.json", "w") as f:
        json.dump(solutions, f, indent=2)

if __name__ == "__main__":
    main()
