from helper import read_data
from copy import copy

def convert_program(line):
   instr = line.split(',')
   res = []
   for i in instr:
      res.append(int(i))
   return res


class IntCode(object):
   def pop(self, n=1):
       try:
           if n == 1:
               return self.program[self.pointer]
           return self.program[self.pointer:self.pointer+n]
       finally:
           self.pointer = self.pointer + n

   def set(self, pointer, data):
       self.program[pointer] = data

   def run(self, program):
       self.program = program
       self.pointer = 0
       while True:
          x = self.exe()
          if x is not None:
              return x

   def exe(self):
       op = self.pop()
       if op == 1:
           self.add()
       elif op == 2:
           self.mul()
       elif op == 3:
           self.input()
       elif op == 99:
           return self.exit()
       else:
           print "Unknown operation", op

   def add(self):
       p1, p2, pres = self.pop(3)
       self.set(pres, self.program[p1] + self.program[p2])

   def mul(self):
       p1, p2, pres = self.pop(3)
       self.set(pres, self.program[p1] * self.program[p2])

   def input(self):
       pres = self.pop()
       self.set(pres, int(raw_input("Input: ")))

   def output(self):
       p1 = self.pop()
       print self.program[p1]

   def exit(self):
       return self.program[0]

def main():
   oprog = read_data("02.txt", converter=convert_program)[0]
   prog = copy(oprog)
   prog[1] = 12
   prog[2] = 2
   ic = IntCode()
   print ic.run(prog)
   for n in xrange(100):
     for v in xrange(100):
        prog = copy(oprog)
        prog[1] = n
        prog[2] = v
        res = ic.run(prog)
        if res == 19690720:
           print n * 100 + v
           return
   print "fail"


if __name__ == '__main__':
   main()

