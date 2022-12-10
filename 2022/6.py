from helper import read_data

s = read_data(f"{__file__.split('.')[0]}.txt")[0]

def a(s, k):
  return [len(set(s[i:min(i+k,len(s)-1)])) for i in range(len(s))].index(k) + k

print(a(s, 4))
print(a(s, 14))


