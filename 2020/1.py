from helper import read_data

s = read_data("1.txt", converter=int)

for x in s:
 for y in s:
  for z in s:
   if x + y +z == 2020:
    print(x, y, z, x*y*z)
