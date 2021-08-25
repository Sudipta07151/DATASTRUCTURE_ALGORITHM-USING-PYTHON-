from GraphClass import *

graph=GraphClass()
graph.add_vertex('A')
graph.add_vertex('C')
graph.add_vertex('B')
graph.add_vertex('D')

graph.print_graph()
graph.add_edge('A','C')
graph.add_edge('A','B')
graph.add_edge('B','C')
graph.add_edge('D','A')
graph.add_edge('D','B')


graph.print_graph()

print(graph.remove_edge('D','A'))
graph.print_graph()


print(graph.remove_edge('D','A'))
graph.print_graph()

print(graph.remove_vertex('A'))

print(graph.remove_vertex('X'))

graph.print_graph()