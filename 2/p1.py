def process_report(val_list):
	loc_unsafe = 0
	incr = False
	decr = False

	for x in range(0, len(val_list)):
		tmp_delta = int(val_list[x]) - int(val_list[x+1])
		if tmp_delta >= 0:
			incr = True
		if tmp_delta <= 0:
			decr = True
		tmp_safe = (1 <= abs(tmp_delta) <= 3)
		if not tmp_safe:
			loc_unsafe += 1
		if incr and decr:
			loc_unsafe += 1
		if x + 1 == len(val_list) - 1:
			break


	if loc_unsafe > 0:
		return False
	else:
		return True		

f = open("puzzle_input.txt", "r")
#f = open("inp_test.txt", "r")
safe = 0
unsafe = 0

for line in f:
	ln = line.split()
	if process_report(ln):
		safe += 1

print(f"Safe reports: {safe}")
