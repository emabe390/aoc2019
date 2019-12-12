from helper import read_data

def fuel_req(mass):
  return int(mass/3-2)


def fuel_req_rec(mass):
  fr = fuel_req(mass)
  if fr < 0:
    return 0
  else:
    return fr + fuel_req_rec(fr)


if __name__ == '__main__':
 data = read_data("01.txt", int)
 sum = 0
 sum_b = 0
 for d in read_data("01.txt", converter=int):
    sum += fuel_req(d)
    sum_b += fuel_req_rec(d)
 print sum
 print sum_b
