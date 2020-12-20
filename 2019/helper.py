def read_data(file, converter=None):
   with open(file) as f:
      data = f.read().strip().split('\n')
   if converter is not None:
      converted = []
      for d in data:
         converted.append(converter(d))
      data = converted
   return data

