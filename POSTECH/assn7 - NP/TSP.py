import sys

# class node:
#     def __init__(self, node_id):
#         self.if = node_id

class edge:
    next = None

    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class graph:
    def __init__(self, node_num):

        self.nodes = []
        for id in range(node_num):
            self.nodes.append(id)

        self.adj = []

        for i in range(node_num):
            self.adj.append(list())
    

    def insert_node(self, s, t, w):

        self.adj[s].append(edge(s,t,w))
        self.adj[t].append(edge(t,s,w))





stage = int(sys.stdin.readline())
output = ""

for i in range(stage):

    node_num, edges_num = map(int,sys.stdin.readline().split())

    G = graph(node_num)

    for e in range(edges_num):
        s,t,w =map(int,sys.stdin.readline().split())
        G.insert_node(s,t,w)
    

    