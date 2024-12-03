import re

f = open("puzzle_input.txt", "r")
raw = f.read()
pattern = r"mul\((\d+),(\d+)\)"
running_total = 0

matches = re.finditer(pattern, raw)
for match in matches:
    num1, num2 = match.group(1), match.group(2)
    #print(f"Found numbers: {num1} and {num2}")
    # num1 and num2 are strings - convert to int if needed
    # int(num1), int(num2)
    running_total += int(num1) * int(num2)

print(f"Running total: {running_total}")