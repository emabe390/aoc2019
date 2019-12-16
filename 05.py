import sys
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
       if isinstance(pointer, list):
           pointer = pointer[0]
       print "setting pointer %s with data %s" % (pointer, data)
       self.program[pointer] = data

   def run(self, program):
       self.program = program
       self.pointer = 0
       while True:
          x = self.exe()
          if x is not None:
              return x

   def get_operation(self):
       op = self.pop()
       opcode = op % 100
       modes = []
       op = int(op / 10)
       while op > 0:
          op = int(op / 10)
          modes.append(op % 10)
       return modes, opcode

   def exe(self):
       modes, op = self.get_operation()
       if op == 1:
           self.add(modes)
       elif op == 2:
           self.mul(modes)
       elif op == 3:
           self.input(modes)
       elif op == 4:
           self.output(modes)
       elif op == 99:
           return self.exit()
       else:
           print "Unknown operation", op
           sys.exit(1)

   def get_data(self, n, modes):
       while len(modes) < n:
          modes.append(0)
       values = []
       for m in modes:
          d = self.pop()
          if m == 0:
              values.append(self.program[d])
          elif m == 1:
              values.append(d)
          else:
              print "Unknown mode"
              sys.exit(1)
       print values
       return values

   def add(self, modes):
       p1, p2, pres = self.get_data(3, modes)
       self.set(pres, p1 + p2)

   def mul(self, modes):
       p1, p2, pres = self.get_data(3, modes)
       self.set(pres, p1 * p2)

   def input(self, modes):
       pres = self.get_data(1, modes)
       self.set(pres, int(raw_input("Input: ")))

   def output(self, modes):
       pres = self.get_data(1, modes)
       print self.program[pres]

   def exit(self):
       return self.program[0]

def main():
   oprog = read_data("05.txt", converter=convert_program)[0]
   prog = copy(oprog)
   ic = IntCode()
   print ic.run(prog)


if __name__ == '__main__':
   main()

