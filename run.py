#!/usr/bin/env python3
import argparse
import csv
from datetime import date
import enum
import importlib
import json
import os
from pathlib import Path
from subprocess import run
import time
from typing import Any
from functools import cache

from tabulate import tabulate

class EXIT_CODES(enum.Enum):
    # Must match utils.EXIT_CODES
    SUCCESS = 0
    NOT_IMPLEMENTED = 38


if os.name == 'posix':
    GREEN = "\033[0;32m"
    RED = "\033[1;31m"
    BLUE = "\033[0;34m"
    RESET = "\033[0;0m"
else:
    GREEN = ""
    RED = ""
    BLUE = ""
    RESET = ""

def success(string):
    return GREEN + str(string) + RESET

def failure(string):
    return RED + str(string) + RESET

def inconclusive(string):
    return BLUE + str(string) + RESET

@cache
def read_solutions_json() -> dict[str, dict[str, dict[str, str]]]:
    with open("sols/solutions.json", "r") as f:
        return json.load(f)

def get_solution(day: str, part: int, test: bool) -> str:
    solutions = read_solutions_json()

    part_str = str(part)
    type_str = "test" if test else "full"
    
    return solutions[day][part_str][type_str]

def run_as_subprocess(days: list[int], parts: list[int], test: bool) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []

    for day in days:
        result = {'Day': f'Day {day[4:]}'}
        for part in parts:
            input_str = "test input" if test else "full input"
            result_header = f"Part {part} ({input_str})"
            command = [f"sols/{day}.py", str(part), "-v"]
            if test:
                command.append("-t")

            script_output = run(command, capture_output=True, text=True)

            if script_output.returncode == EXIT_CODES.NOT_IMPLEMENTED.value:
                result[result_header] = inconclusive("Not implemented")
                continue

            try:
                calculated_sol = json.loads(script_output.stdout.strip())["solution"]
            except json.decoder.JSONDecodeError:
                result[result_header] = failure("No solution found")
                continue

            try:
                actual_sol = get_solution(day, part, test)
            except KeyError:
                result[result_header] = inconclusive(calculated_sol)
                continue

            if calculated_sol == actual_sol:
                execution_time = json.loads(script_output.stdout.strip())["execution_time"]
                result[result_header] = success(f"{calculated_sol}    ({execution_time})") 
            else:
                result[result_header] = failure(calculated_sol)

        results.append(result)

    return results

def main():
    this_year = date.today().year

    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--args",  action="store_true", help="Print args")
    parser.add_argument("-d", "--day",  type=int, help="Advent of code day. Leave blank to run all days.")
    parser.add_argument("-t", "--test", action="store_true", help="Whether to run with test input. If false, runs with full input.")
    parser.add_argument("-p", "--part", type=int, help="Which part to run. Leave blank to run both parts.")
    parser.add_argument("-y", "--year", type=int, default=this_year, help=f"Which year to run. Default is {this_year}")

    args = parser.parse_args()

    if not args.day:
        days = sorted([f.stem for f in Path("sols").glob('*') if f.name.startswith(f"{args.year}") and f.suffix == ".py"])
    else:
        days = [f"{args.year}{args.day:02}"]

    if not args.part:
        parts = [1, 2]
    else:
        parts = [args.part]

    if args.args:
        print(f"year: {args.year}")
        print(f"days: {days}")
        print(f"test: {args.test}")
        print(f"parts: {parts}")

    results = run_as_subprocess(days, parts, args.test)

    print(tabulate(results, headers='keys', tablefmt="github"))

if __name__ == "__main__":
    main()
