from Trees.TreeClass import BinarySearchTree
from BFS import *
from DFS import *

tree = BinarySearchTree()
tree.insert(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
tree.insert(27)
tree.insert(52)
tree.insert(82)

root = tree.get_root()

bfs = BFS(root)
print(bfs.perform_bfs())

dfs=DFS(root)
print(dfs.inorder())
print(dfs.preorder())
print(dfs.postorder())


