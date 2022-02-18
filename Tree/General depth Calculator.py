class Node:
  def __init__(self, value=None, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def tree_depth(tree):
    # null tree situation
    if tree is None:
      return 0
    left_depth = tree_depth(tree.left)
    right_depth = tree_depth(tree.right)
    return 1 + max(left_depth, right_depth)

# define tree
trr = Node('D', left=Node('B', Node('A'), Node('C')), right=Node('E', right=Node('G', Node('F'))))

# evoke the depth calculation method
a = tree_depth(trr)
