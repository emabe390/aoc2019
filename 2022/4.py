from helper import read_data

def split_ass(x):
 a, b = x.split(",")
 a1, a2 = a.split("-")
 b1, b2 = b.split("-")
 return [set(range(int(a1),int(a2)+1)), set(range(int(b1),int(b2)+1))]

s = read_data(f"{__file__.split('.')[0]}.txt", converter=split_ass)




def one(p1, p2):
  return p1 - p2 == set() or p2 - p1 == set()

def two(p1, p2):
  return len(p1-p2) < len(p1) or len(p2-p1) < len(p2)

k = 0
k2 = 0
for p in s:
 k += 1 if one(*p) else 0
 k2 += 1 if two(*p) else 0
print(k)
print(k2)