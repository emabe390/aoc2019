from helper import read_data

def converter(line):
  a, b = line.split('-')
  return (int(a), int(b))

# six digit
# within range
# two adjacent digits are equal
# never decrease

def acceptable(digit):
  if len(str(digit)) != 6:
     return False
  s = " %s " % str(digit)
  prev = None
  for x in s:
    if x == prev:
      break
    prev = x
  else:
    return False
  prev = -1
  for x in str(digit):
    d = int(x)
    if d < prev:
       return False
    prev = d
  return True

# has at least one group of two, but not three
def harder(digit):
  s = str(digit)
  prev = ""
  tmp = ""
  for x in s:
   if prev == x:
     tmp+=prev
   else:
     if len(tmp) == 2:
        return True
     tmp = x
   prev = x
  if len(tmp) == 2:
    return True
  return False

def main():
  start, end = read_data("04.txt", converter=converter)[0]
  d = 0
  e = 0
  for i in xrange(start, end+1):
    if acceptable(i):
      d+=1
      if harder(i):
       e+=1
  print d, e


if __name__ == '__main__':
   main()
