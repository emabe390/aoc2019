from helper import read_data

class pw():
	def __init__(self, text):
		spl = text.split(" ")
		self.fr = int(spl[0].split("-")[0])
		self.to = int(spl[0].split("-")[1])
		self.le = spl[1][0]
		self.pw = spl[2]

	def valid(self):
		count = self.pw.count(self.le)
		return self.fr <= count <= self.to

	def valid2(self):
		a = self.pw[self.fr-1] == self.le
		b = self.pw[self.to-1] == self.le
		if a and b:
			return False
		return a or b
		

s = read_data("2.txt", converter=pw)

print(sum([z.valid() for z in s]))
print(sum([z.valid2() for z in s]))