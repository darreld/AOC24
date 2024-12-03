def apply_problem_dampener(numbers):
    """
    Takes a list of strings representing numbers and generates reports
    by iteratively removing one element at a time.

    Args:
        numbers: List[str] - list of strings representing numbers
    """
    # Make a copy to avoid modifying the original list
    for i in range(len(numbers)):
        # Create a new list excluding the current index
        modified_list = numbers[:i] + numbers[i + 1:]
        # Call external processing function
        fixed = process_report(modified_list)
        if fixed:
            return True
        else:
            continue

    return False


def find_fixable_sequences(numbers):
    """
    Finds sequences that can be made valid by removing one number.
    Valid sequences must be monotonic (all increasing or all decreasing)
    with differences between 1 and 3 inclusive.

    Args:
        numbers: List[int] - list of numbers to check

    Returns:
        list: List of valid sequences after removing one number
    """
    if len(numbers) <= 2:
        return []

    def is_valid_sequence(nums):
        if len(nums) <= 1:
            return True

        diffs = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        # Check if all differences are between 1 and 3 (increasing)
        all_positive = all(1 <= d <= 3 for d in diffs)
        # Check if all differences are between -3 and -1 (decreasing)
        all_negative = all(-3 <= d <= -1 for d in diffs)
        return all_positive or all_negative

    valid_sequences = []
    # Try removing each number one at a time
    for i in range(len(numbers)):
        test_sequence = numbers[:i] + numbers[i + 1:]
        if is_valid_sequence(test_sequence):
            valid_sequences.append(test_sequence)

    return valid_sequences

    valid_sequences = []
    # Try removing each number
    for i in range(len(numbers)):
        test_sequence = numbers[:i] + numbers[i + 1:]
        if is_valid_sequence(test_sequence):
            # Convert back to string format
            valid_sequences.append(' '.join(map(str, test_sequence)))

    return valid_sequences


'''
def apply_problem_dampener(in_list):

    for x in in_list:
        working_list = [i for i in in_list]
        working_list.remove(x)
        fixed = process_report(working_list)
        if fixed:
            return True
        else:
            continue

    return False
'''

def process_report(val_list):
    loc_unsafe = 0
    incr = 0
    decr = 0

    for x in range( len(val_list)):
        tmp_delta = int(val_list[x]) - int(val_list[x+1])
        if tmp_delta >= 0:
            incr += 1
        if tmp_delta <= 0:
            decr += 1
        values_safe = (1 <= abs(tmp_delta) <= 3)
        if not values_safe:
            loc_unsafe += 1
        if incr > 1 and decr > 1:
            loc_unsafe += 1
        # stop processing if we're at the end
        if x + 1 == len(val_list) - 1:
            break

    if loc_unsafe > 0:
        chance = apply_problem_dampener(val_list)
        if chance:
            return True
        else:
            return False
    else:
        return True

#f = open("puzzle_input.txt", "r")
f = open("inp_test.txt", "r")
safe = 0
unsafe = 0

for line in f:
    ln = line.split()
    if process_report(ln):
        safe += 1
    fixes = find_fixable_sequences(ln)
    for cur_ln in range(0, len(fixes)):
        safe += 1

print(f"Safe reports: {safe}")
