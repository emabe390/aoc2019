from helper import read_data

s = read_data(f"{__file__.split('.')[0]}.txt")[1:]

def debug(*msg):
  pass
  #print(*msg)

fz = []
k = []
sizes = {}
class Directory:
  def __init__(self, name, parent=None):
    self.name = name
    self.parent = parent
    self.dirs = {}
    self.files = {}
  
  def get(self, dirname):
    if dirname not in self.dirs:
      self.create_subdir(dirname)
    return self.dirs[dirname]
  
  def get_root(self):
    if self.parent is None:
      return self
    else:
      return self.parent.get_root()
  
  def create_subdir(self, dirname):
    if dirname not in self.dirs:
      debug("Creating", dirname, "in", self.name)
      self.dirs[dirname] = Directory(dirname, self)
  
  def add_file(self, size, filename):
    self.files[filename] = size
    fz.append(size)

  def get_whole_name(self):
    if self.parent is None:
      return self.name
    else:
      return self.parent.get_whole_name() + "/" + self.name

  def calc_size_bad(self):
    mv = sum(self.files.values())
    for d in self.dirs.values():
      mv+=d.calc_size_bad()
    if mv <= 100000:
      k.append(mv)
    sizes[self.get_whole_name()] = mv
    return mv

class Runner:
  def __init__(self, commands):
    self.current_dir = Directory("/")
    self.commands = commands
    self.commands_len = len(commands)
    self.index = 0
    self.directories = {}

  def is_command(self, command):
    return command.startswith("$ ")

  def current_line(self):
    return self.commands[self.index]
  
  def next_command_index(self):
    for i in range(self.index + 1, self.commands_len):
      if self.is_command(self.commands[i]):
        return i
  
  def current_command_and_output(self):
    return self.commands[self.index:self.next_command_index()]

  def parse_cd(self):
    dirname = self.current_line()[len("$ cd "):]
    debug("cd", dirname)

    if self.current_dir == None:
      print("inital dir:", dirname)
      self.current_dir = Directory(dirname)
    elif dirname == "..":
      self.current_dir = self.current_dir.parent
      if self.current_dir == None:
        raise NotImplementedError
    else:
      self.current_dir = self.current_dir.get(dirname)

  def parse_ls(self):
    output = self.current_command_and_output()[1:]
    debug(self.current_dir.name, output)
    for line in output:
      a, b = line.split()
      if a == "dir":
        self.current_dir.create_subdir(b)
      else:
        self.current_dir.add_file(int(a), b)
      self.index += 1

  def run(self):
    while self.index < self.commands_len:
      cl = self.current_line()
      if self.is_command(cl):
        if cl.startswith("$ cd "):
          self.parse_cd()
        elif cl == "$ ls":
          self.parse_ls()
        else:
          raise NotImplementedError
      
      self.index += 1
    self.get_size_bad()

  def get_size_bad(self):
    return self.current_dir.get_root().calc_size_bad()
    

r = Runner(s)
r.run()
print(sum(k))
total =  70000000
sought = 30000000
free_space = total - sizes["/"]
needed = sought - free_space
best = None
bestval = None
for k,v in sizes.items():
  if v < needed:
    continue
  if best == None:
    best = k
    bestval = v
    print(v, " -> ")
  elif bestval > v:
    best = k
    bestval = v
    print(v, " -> ")

print("Space after removing:", free_space + v)
print("Best removal:", bestval)
