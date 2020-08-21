from typing import List

class Node:
  def __init__(self, x):
    # integer values
    self.val = x
    self.left = None
    self.right = None

  def __str__(self):
    return str(self.val)

'''
Input: string of BST array
Output: BST array
e.g. "[1, 2, 3, 4, 5]" -> [1, 2, 3, 4, 5]
'''
def str_to_array(string: str) -> List[int]:
  # now "[1, 2, 3, None, None, 4, 5, None, 6]"
  output = string.strip('[] ').split(',')
  if output == [""]: return []
  # now ['1', ' 2', ' 3', ' None', ' None', ' 4', ' 5', ' None', ' 6']
  output = [w.strip() for w in output]
  # now ['1', '2', '3', 'None', 'None', '4', '5', 'None', '6']
  output = [None if w=="None" or w=="" else int(w) for w in output]
  # now [1, 2, 3, None, None, 4, 5, None, 6]
  return output

'''
Input: array of node values
e.g. [1, 2, 3, None, None, 4, 5]
        1
      /   \
    2       3
          /   \
        4       5

Output: root of binary tree
'''
def array_to_bst(arr: List[int]) -> Node:
  nodes = [None for _ in arr]
  n = len(arr)
  # handle empty case
  if n == 0:
    return None

  for i in range(n):
    if arr[i]:
      nodes[i] = Node(arr[i])

  def left(i: int) -> int:
    return 2*i + 1
  def right(i: int) -> int:
    return 2*i + 2
  def parent(i: int) -> int:
    return (i-1)//2

  for i in range(n):
    if nodes[i]:
      if left(i) < n:
        nodes[i].left = nodes[left(i)]
      if right(i) < n:
        nodes[i].right = nodes[right(i)]

  # return root
  return nodes[0]  

'''
Input: root node
Output: level order traversal
e.g. root of [1, 2, 3] -> [[1], [2, 3]]
'''
def level_traversal(root: Node) -> List[List[int]]:
  if root is None:
    return []
  output = []
  level = [root] 
  next_level = []
  
  while len(level) > 0:
    # first, append current level's node vals to our output
    curr_vals = []
    for node in level:
      if node is not None:
        curr_vals.append(node.val)
      else:
        curr_vals.append(None)
    output.append(curr_vals)

    # next, find next level of level traversal
    for node in level:
      if node:
        next_level.append(node.left)
        next_level.append(node.right)
    level = next_level
    next_level = []

  # trim the last empty level that we traversed through before terminating
  output.pop()
  return output
'''
Input: level order traversal of a tree 
Output: array representation of the tree
e.g. [[1], [2, 3], [None, None, 4,5]] -> [1, 2, 3, None, None, 4, 5]
'''
def level_traversal_to_array(level_order: List[List[int]]) -> List[int]:
  output = []
  for level in level_order:
    output += level
  return output

# sanity check of processing string to bst, and bst back to str
print("Starting string: ")
a = str_to_array("   [1,2,3,None,None, 4, 5]")
print(a)

print("BST root: ")
b = array_to_bst(a)
print(b)

print("Level order traversal of BST: ")
c = level_traversal(b)
print(c)

print("Recovered BST array from traversal: ")
d = level_traversal_to_array(c)
print(str(d))
