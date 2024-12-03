# Regular expression with capturing groups
#mul\((\d+),(\d+)\)

# Example usage with Python's re module
import re

text = "some text mul(123,456) more text mul(7,8)"
pattern = r"mul\((\d+),(\d+)\)"

matches = re.finditer(pattern, text)
for match in matches:
    num1, num2 = match.group(1), match.group(2)
    print(f"Found numbers: {num1} and {num2}")
    # num1 and num2 are strings - convert to int if needed
    # int(num1), int(num2)