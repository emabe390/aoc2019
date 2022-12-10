from helper import read_data

s = read_data(f"{__file__.split('.')[0]}.txt")

elfs = {}
current_elf = []
k = 0
max = -1
cals = []
for x in s:
	if x == "":
		elfs[k] = current_elf
		c = sum(current_elf)
		if c > max:
			max = c
		cals.append(c)
		k+=1
		current_elf = []
	else:
		current_elf.append(int(x))

print(max)
print(sum(sorted(cals)[-3:]))