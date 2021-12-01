from helper import read_data

s = read_data("1.txt", converter=int)

z = 0
for i in range(len(s)):
	if i+1 >= len(s):
		break
	if s[i] < s[i+1]:
		z+=1
print(z)

z = 0
for i in range(len(s)):
	if i+3 >= len(s):
		break
	if s[i] < s[i+3]:
		z+=1
print(z)