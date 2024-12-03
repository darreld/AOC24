
#f = open("inp.txt", "r")
f = open("puzzle_input.txt", "r")
left = []
rt = []


for myline in f:
#	tmpl, tmpr = myline.split("   ")
	tmpl, tmpr = myline.split()
	left.append(int(tmpl))
	rt.append(int(tmpr))

left.sort()
rt.sort()
totlist =[]
total = 0;

tmpdist = 0;

for x in range(0, len(left)):
	if left[x] > rt[x]:
		tmpdist = left[x] - rt[x]
		totlist.append(tmpdist)
	elif rt[x] > left[x]:
		tmpdist = rt[x] - left[x]
		totlist.append(tmpdist)
	else:
		totlist.append(0)
	
total = sum(totlist)
lenlist = len(totlist)

print(f"Total({lenlist}) is {total}")


			