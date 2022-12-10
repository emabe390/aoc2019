from helper import read_data, gen_splitter

def split_halfway(x):
 return ["".join(x[:len(x)//2]),"".join(x[len(x)//2:])]

s = read_data(f"{__file__.split('.')[0]}.txt", converter=split_halfway)

def get_prio(char):
  o = ord(char)
  if o > 90:
    return o - 96
  return o - 64 + 26
  

def get_common(a, b):
  return list(set(a) & set(b))[0]

def get_common2(a,b,c):
  try:
     x = set(a) & set(b)
     y = set(c) & x
     return list(y)[0]
  except:
     print(a, b, c)
     raise

x = 0
for dp in s:
  x+=(get_prio(get_common(*dp)))
print(x)


current_group = []
y = 0
for dp in s:
  current_group.append("".join(dp))
  if len(current_group) == 3:
    y+=get_prio(get_common2(*current_group))
    current_group = []
print(y)
