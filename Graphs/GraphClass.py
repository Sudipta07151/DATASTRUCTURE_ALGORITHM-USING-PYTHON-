class GraphClass:
    def __init__(self):
        self.adj_list={}

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]
            return True
        return False

    def remove_vertex(self,vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list:
            print(f'{vertex} : {self.adj_list[vertex]}')

    def add_edge(self,vertex1,vertex2):
        if vertex1 not in self.adj_list.keys() or vertex2 not in self.adj_list.keys():
            return False
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)
        return True

    def remove_edge(self,vertex1,vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            if vertex2 in self.adj_list[vertex1] and vertex1 in self.adj_list[vertex2]:
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
                return True
        return False
