from TreeClass import *

tree=BinarySearchTree()
tree.insert(47)
tree.insert(21)
tree.insert(55)
tree.insert(90)
tree.insert(15)
tree.insert(20)

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)


print(tree.contains_value(47))


