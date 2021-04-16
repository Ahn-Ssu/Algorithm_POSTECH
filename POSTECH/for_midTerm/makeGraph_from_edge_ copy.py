# 초기 입력 노드수, 엣지수 
# 그 이후 엣지 입력 됨 

class graph:
    adj_list = [] 
    node_list = []
    node_num = 0 
    edge_num = 0 

    def __init__(self, node_num, edge_num):
        self.node_num = node_num
        self.edge_num = edge_num
        for i in range(self.node_num):
            self.adj_list.append(list([]))
            self.node_list.append(node(i))
    
    def add_edge(self, node1, node2):
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1) # undirect인 경우

class node:
    node_id = None
    dist = float('inf')
    prev = None
    
    def __init__(self, id):
        self.node_id = id

node_num, edge_num=input().split()

print(node_num)
print(edge_num)
node_num = int(node_num)
edge_num = int(edge_num)

G = graph(node_num, edge_num)

for i in range(edge_num):
    node1, node2 = input().split()
    G.add_edge(int(node1), int(node2))
print(G.adj_list)
print(G.node_list)
for i in range(G.node_num):
    print(G.node_list[i].dist)