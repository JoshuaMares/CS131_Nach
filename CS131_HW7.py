class Node:
  def __init__(self, val):
    self.value = val
    self.next = None

class HashTable:
  def __init__(self, buckets):
    self.array = [None] * buckets
  def insert(self, val):
    bucket = hash(val) % len(self.array)
    tmp_head = Node(val)
    tmp_head.next = self.array[bucket]
    self.array[bucket] = tmp_head

ht = HashTable(5)
for i in range(21):
  ht.insert(i)

def gen(hash_table):
  for i in range(len(hash_table.array)):
    tmp = hash_table.array[i]
    while tmp != None:
      yield tmp
      tmp = tmp.next

print("gen output")
x = gen(ht)
for n in x:
  print(n.value)

class OurIterator:
  def __init__(self, arr):
    self.arr = arr
    self.pos = 0
    self.list = self.arr[self.pos]
  def __next__(self):
    if self.list != None:
      val = self.list
      self.list = self.list.next
      return val
    else:
      self.pos += 1
      if self.pos < len(self.arr):
        self.list = self.arr[self.pos]
        val = self.list
        self.list = self.list.next
        return val
      else:
        raise StopIteration

class HashTable:
  def __init__(self, buckets):
    self.array = [None] * buckets
  def __iter__(self):
    it = OurIterator(self.array)
    return it
  def insert(self, val):
    bucket = hash(val) % len(self.array)
    tmp_head = Node(val)
    tmp_head.next = self.array[bucket]
    self.array[bucket] = tmp_head

ht = HashTable(5)
for i in range(21):
  ht.insert(i)

print("iterator output")
for n in ht:
  print(n.value)

print("iterator dunder output")
iter = ht.__iter__()
try:
  while True:
    i = iter.__next__()
    print(i.value)
except StopIteration:
  pass

class HashTable:
  def __init__(self, buckets):
    self.array = [None] * buckets
  def __iter__(self):
    it = OurIterator(self.array)
    return it
  def insert(self, val):
    bucket = hash(val) % len(self.array)
    tmp_head = Node(val)
    tmp_head.next = self.array[bucket]
    self.array[bucket] = tmp_head
  def forEach(self, func):
    for i in range(len(self.array)):
      tmp = self.array[i]
      while tmp != None:
        func(tmp)
        tmp = tmp.next

ht = HashTable(5)
for i in range(21):
  ht.insert(i)

print("forEach output")
ht.forEach(lambda x: print(x.value))
