class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  def __str__(self):
    return str(f'value: {self.value}, left {self.left}, right: {self.right}')

  def depth_first_for_each(self, cb):
    if self.left == None and self.right == None:
      return cb(self.value)

    #get first value set up
    cb(self.value)

    #left tree
    def recurse_left_tree(output):
      cb(output.value)
      if output.left == None and output.right != None:
        cb(output.right.value)
        return
      recurse_left_tree(output.left)

    #right tree
    def recurse_right_tree(output):
      cb(output.value)
      if output.left == None and output.right == None:
        return
      recurse_right_tree(output.right)

    #calls to the two trees
    recurse_left_tree(self.left)
    recurse_right_tree(self.right)
       

  def breadth_first_for_each(self, cb):
    if self.left == None and self.right == None:
      return cb(self.value)

    # bool_v = False
    arr = []
    arr.append(self.value)

    def tree(output):

      if output == None:
        return

      if output.left != None:
        arr.append(output.left.value)

      if output.right != None:
        arr.append(output.right.value)

      tree(output.left)
      tree(output.right)

    tree(self)
    
    for i in arr:
      cb(i)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
