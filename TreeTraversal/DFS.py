
class DFS:
    def __init__(self, root):
        self.root=root

    def inorder(self):
        results=[]
        order=[]

        def traverse(vertex=self.root):
            if vertex.left is not None:
                order.append('LEFT')
                traverse(vertex.left)
            order.append('PARENT')
            results.append(vertex.value)
            if vertex.right is not None:
                order.append('RIGHT')
                traverse(vertex.right)
        traverse()
        return order,results

    def preorder(self):
        results=[]
        order = []
        def traverse(vertex=self.root):
            order.append('PARENT')
            results.append(vertex.value)
            if vertex.left is not None:
                order.append('LEFT')
                traverse(vertex.left)
            if vertex.right is not None:
                order.append('RIGHT')
                traverse(vertex.right)
        traverse()
        return order,results

    def postorder(self):
        results=[]
        order=[]
        def traverse(vertex=self.root):
            if vertex.left is not None:
                order.append('LEFT')
                traverse(vertex.left)
            if vertex.right is not None:
                order.append('RIGHT')
                traverse(vertex.right)
            order.append('PARENT')
            results.append(vertex.value)

        traverse()
        return order,results
