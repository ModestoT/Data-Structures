"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    val = self.head
    count = 0
    # Loops through the linked list until the nodes next value is None, counts each node for the length
    while val:
      count +=1
      val = val.next
    
    return count

  def add_to_head(self, value):
    new_node = ListNode(value) # Store a new ListNode instance incase one has not been made already
  
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node

    else:
      old_head = self.head # store the old head node for use when setting the new head node
      self.head.insert_before(value)

      self.head = old_head.prev

  def remove_from_head(self):
    if not self.head and not self.tail:
      return None

    if not self.head.next:
      head = self.head

      self.head = None
      self.tail = None
      
      return head.value
    else:
      old_head = self.head
      self.head = self.head.next

      return old_head.value

  def add_to_tail(self, value):
    new_node = ListNode(value)

    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node

    else:
      old_tail = self.tail

      self.tail.insert_after(value)

      self.tail = old_tail.next

  def remove_from_tail(self):
    if not self.head and not self.tail:
      return None
    
    if self.head == self.tail:
      old_tail = self.tail

      self.head = None
      self.tail = None

      return old_tail.value
    
    else:
      old_tail = self.tail

      self.tail = old_tail.prev

      return old_tail.value

  def move_to_front(self, node):
    current = node
    self.delete(node)
    self.add_to_head(current.value)

  def move_to_end(self, node):
    current = node
    self.delete(node)
    self.add_to_tail(current.value)

  def delete(self, node):
    # checks if the node is the only node in the linked list
    if not node.prev and not node.next:
      self.head = None
      self.tail = None
    # checks if the node has anything behind it, if not it's the head
    elif not node.prev:
      node.next.prev = node.prev
      self.head = node.next
    # checks if the node has anything after it, if not it's the tail
    elif not node.next:
      self.tail = node.prev
      node.prev.next = node.next
    # catches all the deletes for nodes that are not the head or the tail
    else:
      node.next.prev = node.prev
      node.prev.next = node.next

  def get_max(self):
    max_value = 0
    val = self.head

    while val:
      if val.value > max_value:
        max_value = val.value
      val = val.next
    return max_value

# ln = ListNode(1)
# dll = DoublyLinkedList(ln)


# dll.add_to_head(10)

# print(len(dll))