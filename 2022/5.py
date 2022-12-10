def read_data(file, converter=None):
   with open(file) as f:
      data = f.read().split('\n')
   if converter is not None:
      converted = []
      for d in data:
         converted.append(converter(d))
      data = converted
   return data

def clean_line(line):
  spl = line.split()
  return [int(spl[1]), int(spl[3]), int(spl[5])]

def arg_box(line):
  return [line[x] for x in range(1,len(line), 4)]

s = read_data(f"{__file__.split('.')[0]}.txt")

mid = s.index('')
boxes = [arg_box(x) for x in s[:mid-1]]
piles = {int(x):[] for x in arg_box(s[mid-1])}
instructions = [clean_line(x) for x in s[mid+1:] if x]

for x in reversed(boxes):
 for i in range(len(x)):
  v = x[i]
  if v != " ":
    piles[i+1].append(v)

def peek(pile):
  return piles[pile][-1]

def peek_all():
  return "".join(peek(x) for x in sorted(piles))
  

def put(pile, value):
  piles[pile].append(value)

def pop(pile):
  return piles[pile].pop()

def execute(instr):
  n,f,d = instr
  for _ in range(n):
    put(d, pop(f))
    
for instr in instructions:
  execute(instr)

print(peek_all())