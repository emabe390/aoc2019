from helper import read_data
from copy import copy

def convert_program(line):
   instr = line.split(',')
   res = []
   for i in instr:
      res.append(int(i))
   return res

def exe(pointer, prog):
   data = prog[pointer:pointer+4]
   if len(data) > 0:
     op = data[0]
   if len(data) > 1:
     p1 = data[1]
   if len(data) > 2:
     p2 = data[2]
   if len(data) > 3:
     pres = data[3]
   if op == 1:
      prog[pres] = prog[p1] + prog[p2]
   elif op == 2:
      prog[pres] = prog[p1] * prog[p2]
   elif op == 99:
      return False
   return True

def run(prog):
   pointer = 0
   while exe(pointer, prog):
      pointer += 4

def main():
   oprog = read_data("02.txt", converter=convert_program)[0]
   prog = copy(oprog)
   prog[1] = 12
   prog[2] = 2
   run(prog)
   print prog[0]
   for n in xrange(100):
     for v in xrange(100):
        prog = copy(oprog)
        prog[1] = n
        prog[2] = v
        run(prog)
        if prog[0] == 19690720:
           print n * 100 + v
           return
   print "fail"

if __name__ == '__main__':
   main()

