
class BFS:
    def __init__(self, root):
        self.queue=[]
        self.results=[]
        self. queue.append(root)

    def perform_bfs(self):
        while len(self.queue) > 0:
            current_node = self.queue.pop(0)
            self.results.append(current_node.value)
            if current_node.left is not None:
                self.queue.append(current_node.left)
            if current_node.right is not None:
                self.queue.append(current_node.right)

        return self.results

