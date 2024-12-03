#f = open("inp.txt", "r")
f = open("puzzle_input.txt", "r")
left = []
rt = []


for myline in f:
	tmpl, tmpr = myline.split("   ")
	left.append(int(tmpl))
	rt.append(int(tmpr))

left.sort()
rt.sort()
totlist =[]
total = 0;
simscore = 0

for x in range(0, len(left)):
	tmp_occ = rt.count(left[x])
	if (tmp_occ == 0):
		simscore += 0
	else:
		simscore += left[x] * tmp_occ

print(f"simscore = {simscore}")		






