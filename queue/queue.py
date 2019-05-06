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

  def add_tail(self, value):
    new_node = Node(value)

    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node

    else:
      self.tail.set_next(new_node)

      self.tail = new_node
  
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

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    pass
  
  def dequeue(self):
    pass

  def len(self):
    pass
