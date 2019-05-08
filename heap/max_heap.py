class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)

    self._bubble_up(len(self.storage)-1)

  def delete(self):
    if len(self.storage) > 1:
      temp = self.storage[0]

      self.storage[0] = self.storage[-1]
      self.storage.pop()

      self._sift_down(0)

      return temp
    else:
      temp = self.storage[0]
      self.storage.pop()
      return temp

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      parent = (index - 1) // 2

      if self.storage[parent] < self.storage[index]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

        index = parent
      else:
        break

  def _sift_down(self, index):
    while index < (len(self.storage) - 1):
      left = (2 * index) + 1
      right = (2 * index) + 2
     
      if left >= len(self.storage) or right >= len(self.storage):
        break
      else:
        if self.storage[left] < self.storage[right]:
          if self.storage[right] > self.storage[index]:
            self.storage[right], self.storage[index] = self.storage[index], self.storage[right]
            index = right
          else:
            break
        else:
          if self.storage[left] > self.storage[index]:
            self.storage[left], self.storage[index] = self.storage[index], self.storage[left]
            index = left
          else:
            break 
