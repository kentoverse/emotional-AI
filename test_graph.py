import pygraphviz as pgv

G = pgv.AGraph()
G.add_node('a')
G.add_edge('a', 'b')
G.layout()
G.draw('test.png')
