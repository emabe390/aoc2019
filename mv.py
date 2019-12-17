

def decode(file):
   with open(file) as f:
     data = f.read()
   data = data[1:] + data[0]
   with open(file, 'w') as f:
      f.write(data)

def encode(file):
   with open(file) as f:
      data = f.read()
   data = data[-1] + data[:-1]
   with open(file, 'w') as f:
      f.write(data)


if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'e':
        print 'encoding' + sys.argv[2]
        encode(sys.argv[2])
    elif sys.argv[1] == 'd':
        print 'decoding' + sys.argv[2]
        decode(sys.argv[2])
    else:
        print "incorrect usage"
