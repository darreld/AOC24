import re


def remove_between_markers(text):
    """
    Removes all text between 'don't()' and 'do()' markers, inclusive.

    Args:
        text (str): Input text

    Returns:
        str: Text with all content between markers removed
    """
    result = ""
    skip = False
    i = 0

    while i < len(text):
        # Check for don't() marker
        if text[i:i + 7] == "don't()":
            skip = True
            i += 7
            continue

        # Check for do() marker
        if text[i:i + 4] == "do()":
            skip = False
            i += 4
            continue

        # Add character if we're not skipping
        if not skip:
            result += text[i]

        i += 1

    return result

f = open("puzzle_input.txt", "r")
raw = f.read()
cleaned = remove_between_markers(raw)
pattern = r"mul\((\d+),(\d+)\)"
running_total = 0

matches = re.finditer(pattern, cleaned)
for match in matches:
    num1, num2 = match.group(1), match.group(2)
    #print(f"Found numbers: {num1} and {num2}")
    # num1 and num2 are strings - convert to int if needed
    # int(num1), int(num2)
    running_total += int(num1) * int(num2)

print(f"Running total: {running_total}")