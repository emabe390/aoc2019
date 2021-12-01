from helper import read_data

def rowsplit(line):
    return [x for x in line]

def calc_trees(dx, dy):
    x = 0
    y = 0
    trees = 0

    while True:
        trees += 1 if data[y][x % len(data[y])] == '#' else 0 

        y += dy
        x += dx
        if y >= len(data):
            break
    return trees

def delt():
    deltas = [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]
    s = 1
    for dx, dy in deltas:
        s *= calc_trees(dx, dy)
    return s

data = read_data("3.test", rowsplit)
print calc_trees(3, 1)
print delt()

data = read_data("3.txt", rowsplit)
print calc_trees(3, 1)
print delt()
