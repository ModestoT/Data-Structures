class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value
  
  def get_next(self):
    return self.next_node
  
  def set_next(self, new_next):
    self.next_node = new_next


class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  # def add_head(self, value):
  #   new_node = Node(value)

  #   if not self.head and not self.tail:
  #     self.head = new_node
  #     self.tail = new_node

  #   else:
  #     self.head.set_next(new_node)

  #     self.head = new_node
    
  def add_tail(self, value):
    new_node = Node(value)

    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node

    else:
      self.tail.set_next(new_node)

      self.tail = new_node
  
  # def remove_tail(self):
  #   if not self.head and not self.tail:
  #     return None
    
  #   if self.head == self.tail:
  #     old_tail = self.tail

  #     self.head = None
  #     self.tail = None

  #     return old_tail
    
  #   else:
  #     old_tail = self.tail

  #     self.tail = None

  def remove_head(self):
    if not self.head and not self.tail:
      return None

    if not self.head.get_next():
      head = self.head

      self.head = None
      self.tail = None
      
      return head.get_value()
    else:
      old_head = self.head
      self.head = self.head.get_next()

      return old_head.get_value()
  
  def get_head(self):
    return self.head.get_value()
  
  def get_tail(self):
    return self.tail.get_value()

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    return self.storage.add_tail(item)
  
  def dequeue(self):
    return self.storage.remove_head()

  def len(self):
    val = self.storage.head
    count = self.size

    while val:
      count += 1
      val = val.get_next()
    
    return count

q = Queue()

q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
q.enqueue(8)
q.enqueue(10)
q.enqueue(12)


print(q.len())
# print(q.storage.get_head(), q.storage.get_tail())
print(q.dequeue())