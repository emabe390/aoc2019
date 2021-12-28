import sys

from helper import read_data, gen_converter


s = read_data("2.txt", converter=gen_converter(str, int))

class Instruction:
    def get_vertical(self):
        return self.vertical * self.scale

    def get_aim(self):
        return self.get_vertical()

    def get_horizontal(self):
        return self.horizontal * self.scale

    def __init__(self, direction_name, direction_scale):
        self.vertical = 0
        self.horizontal = 0
        self.scale = direction_scale
        if direction_name == 'down':
            self.vertical = 1
        elif direction_name == 'up':
            self.vertical = -1
        elif direction_name == 'forward':
            self.horizontal = 1
        elif direction_name == 'backward':
            self.horizontal = -1
        else:
            print(f"ERROR: invalid direction {direction_name}")
            sys.exit(1)

instructions = [Instruction(x, y) for x, y in s]

horizontal = sum(d.get_horizontal() for d in instructions)
vertical = sum(d.get_vertical() for d in instructions)

print(f"{horizontal} * {vertical} = {horizontal * vertical}")

class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.vertical = 0
        self.aim = 0

    def handle_instructions(self, instruction_list):
        for instruction in instruction_list:
            self.handle_instruction(instruction)

    def handle_instruction(self, instruction):
        delta_horizontal = instruction.get_horizontal()
        aim = instruction.get_aim()

        self.aim += aim
        self.horizontal += delta_horizontal
        self.vertical += self.aim * delta_horizontal


sub = Submarine()

sub.handle_instructions(instructions)

print(f"{sub.horizontal} * {sub.vertical} = {sub.horizontal * sub.vertical}")