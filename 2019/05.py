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
    def __init__(self):
        self.pointer = None
        self.program = None
        self.set_input = None

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
        self.program[pointer] = data

    def run(self, program):
        self.program = program
        self.pointer = 0
        while True:
            x = self.exe()
            if x is not None:
                return x
        self.set_input = None

    def get_operation(self):
        op = self.pop()
        operation_code = op % 100
        modes = int(op / 100)
        return modes, operation_code

    def parse_modes(self, n, modes_int):
        modes = []
        for i in xrange(n):
            modes.append(modes_int%10)
            modes_int = int(modes_int/10)
        return modes

    def exe(self):
        #print "prog:", self.program[self.pointer:self.pointer+4]
        modes, op = self.get_operation()
        if op == 1:
            self.add(modes)
        elif op == 2:
            self.mul(modes)
        elif op == 3:
            self.input(modes)
        elif op == 4:
            self.output(modes)
        elif op == 5:
            self.jit(modes)
        elif op == 6:
            self.jif(modes)
        elif op == 7:
            self.lt(modes)
        elif op == 8:
            self.eq(modes)
        elif op == 99:
            return self.exit()
        else:
            print "Unknown operation", op
            sys.exit(1)

    def get_data(self, n, modes_int, special=None):
        if special is None:
            special = []
        modes = self.parse_modes(n, modes_int)
        #print modes, modes_int, self.program[self.pointer:self.pointer+n]
        values = []
        for c, m in enumerate(modes):
            d = self.pop()
            if c + 1 in special:
                m = 1-m
            if m == 0:
                values.append(self.program[d])
            elif m == 1:
                values.append(d)
            else:
                print "Unknown mode"
                sys.exit(1)
        #print values
        if len(values) == 1:
            return values[0]
        return values

    def add(self, modes):
        p1, p2, pres = self.get_data(3, modes, special=[3])
        #print p1, p2, pres
        self.set(pres, p1 + p2)

    def mul(self, modes):
        p1, p2, pres = self.get_data(3, modes, special=[3])
        self.set(pres, p1 * p2)

    def input(self, modes):
        pres = self.get_data(1, modes, special=[1])
        self.set(pres, self.get_input())

    def get_input(self):
        return self.set_input if self.set_input is not None else int(raw_input("Input: "))

    def jit(self, modes):
        data, pointer = self.get_data(2, modes)
        if data != 0:
            self.pointer = pointer

    def jif(self, modes):
        data, pointer = self.get_data(2, modes)
        if data == 0:
            self.pointer = pointer

    def lt(self, modes):
        a, b, pres = self.get_data(3, modes, special=[3])
        self.set(pres, 1 if a < b else 0)

    def eq(self, modes):
        a, b, pres = self.get_data(3, modes, special=[3])
        self.set(pres, 1 if a == b else 0)

    def output(self, modes):
        pres = self.get_data(1, modes)
        print pres

    def exit(self):
        return self.program[0]

def main():
    prog = read_data("05.txt", converter=convert_program)[0]
    prog_1 = copy(prog)
    prog_2 = copy(prog)
    ic = IntCode()
    ic.set_input = 1
    ic.run(prog_1)
    ic.set_input = 5
    ic.run(prog_2)


if __name__ == '__main__':
    main()

