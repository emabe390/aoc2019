def read_data(file, converter=None):
   with open(file) as f:
      data = f.read().strip().split('\n')
   if converter is not None:
      converted = []
      for d in data:
         converted.append(converter(d))
      data = converted
   return data

def gen_splitter(split_on=" "):
   def foo(data):
      return data.split(split_on)
   return foo

def gen_converter(*args):
   def foo(data):
      res = []
      for data_type, data in zip(args, data.split(" ")):
         if data_type is None:
            continue
         res.append(data_type(data))
      return res
   return foo