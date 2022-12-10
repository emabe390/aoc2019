from helper import read_data, gen_splitter

s = read_data(f"{__file__.split('.')[0]}.txt", converter=gen_splitter())

rock = ["A", "X"]
paper = ["B", "Y"]
scissors = ["C", "Z"]

value = {"r": 1, "p": 2, "s": 3}
gv = {"r": "p", "p": "s", "s": "r"}
gl = {"r": "s", "s": "p", "p": "r"}

def RPS(val):
   if val in rock:
      return "r"
   elif val in paper:
      return "p"
   elif val in scissors:
      return "s"
   else:
      return val

def winner(opp, you):
  o = RPS(opp)
  y = RPS(you)
  if o == y:
    return 3
  if o == "r" and y == "p" or o == "p" and y == "s" or o == "s" and y == "r":
    return 6
  return 0

def calc_score(opp, you):
  return winner(opp, you) + value[RPS(you)]

def calc_score2(opp, you):
  o = RPS(opp)
  if you == "X":
    y = gl[o]
	# lose
  elif you == "Y":
    y = o
    # draw
  else:
    y = gv[o]
    # win
  return calc_score(o,y)
   
a = 0
b = 0
for x in s:
 a+=calc_score(*x)
 b+=calc_score2(*x)

print(a)
print(b)