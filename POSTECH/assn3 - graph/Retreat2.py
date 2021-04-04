import sys
sys.setrecursionlimit(10**6)


class AdjNode:
    def __init__(self, V_id, weight=1):
        self.id = V_id
        self.next = None
        self.weight = weight

class Vertex:
    def __init__(self, id,  visited=False, dist=sys.maxsize):
        self.dist = dist
        self.visited = visited
        self.idx_ = None
        self.id = id
        self.next = None

class Graph:
    def __init__(self, num):
        self.V_num = num
        self.Adj = [None] * self.V_num
        self.VertexList = [None] * self.V_num
        for i in range(self.V_num):
            self.VertexList[i] = Vertex(id = i)
        
    # Add edges
    def add_edge(self, s, d, w):
        node = AdjNode(d, w)
        node.next = self.Adj[s]
        self.Adj[s] = node
        

        node = AdjNode(s, w)
        node.next = self.Adj[d]
        self.Adj[d] = node

    # Print the graph
    def print_Adj(self):
        for i in range(self.V_num):
            print("Vertex [" + str(i) + "] :", end="")
            temp = self.Adj[i]
            while temp:
                print(" --{}--> [{}]".format(temp.weight,temp.id), end="")
                temp = temp.next
            print()


def DFS(G, vertex, parent):
    global min_W, find_idx

    vertex.visited = True
    vertex.idx_ = find_idx
    find_idx += 1 

    result = vertex.idx_

    next_V = G.Adj[vertex.id]

    while next_V:

        if next_V.id == parent.id:
            next_V = next_V.next
            continue

        if G.VertexList[next_V.id].visited == False :

            low = DFS(G, G.VertexList[next_V.id], vertex)
        
            if low > vertex.idx_ :
                ans_list.append((vertex.id, next_V.id))

            result = min(result, low)
        
        else:
            result = min(result, G.VertexList[next_V.id].id)


        next_V = next_V.next

    return result
        


stage = int(sys.stdin.readline())
output = ""

for iteration in range(stage): # 입력한 테스트 케이스 iteration 
    find_idx = 1
    node_num, edge_num = tuple(map(int,sys.stdin.readline().split()))

    # if node_num == (edge_num +1) :
    #     E = [0] * edge_num

    #     for idx in range(edge_num):
    #         E[idx] = tuple(map(int,sys.stdin.readline().split()))
        
    #     for _, __, w in E:
    #         min_W = min(min_W, w)

    #     output += "%s\n"%min_W

    # else:
    
    graph = Graph(node_num)
    s_len = sys.maxsize
    E = [0] * edge_num
    
    for idx in range(edge_num):
        E[idx] = tuple(map(int,sys.stdin.readline().split()))
    # E = ((0,1), (1,4), (4,5), (5,2), (2,0), (2,3), (3,6), (6,9), (9,8), (8,10), (10,7), (10,12), (12,13), (11,13), (11,9))
    for u, v, w in E:
        graph.add_edge(u,v,w)
        

    ans_list = [] 
    # graph.print_Adj()
    for i in range(1,node_num):
        DFS(graph, graph.VertexList[i], graph.VertexList[0])

    # for node in graph.VertexList:
    #     print("id : {}, visit idx_ : {}".format(node.id, node.idx_))
    # if min_W == sys.maxsize:
    #     output += "%s\n"%-1
    # else:
    #     output += "%s\n"%min_W
    if len(ans_list):
        min_W = sys.maxsize
        
        for u, v in ans_list:
            temp = graph.Adj[u]

            while temp:
                

                if temp.id == v :
                    min_W = min(min_W, temp.weight)
                
                temp = temp.next

        output += "%s\n"%min_W
    else:
        output += "-1\n"

        

print(output, end="")

# ((0,1),(1,2),(0,2))
#((0,1), (1,2),(1,3),(3,2),(2,4),(4,1)) 
#((0,1),(0,2),(1,2),(1,3),(3,4),(1,4),(4,5),(2,7),(2,6)) 
#((0,1),(0,2),(1,3),(1,4),(4,5),(2,7),(2,6))
#( (0,1), (0,2), (1,3), (1,4), (2,4), (4,5))
# ( (0,1), (0,2), (1,3), (1,4), (2,4), (4,5), (2,7),(2,6),(6,7))
# ( (0,1), (1,2))
# ((0,1), (1,4), (4,5), (5,2), (2,0), (2,3), (3,6), (6,9), (9,8), (8,10), (10,7), (10,12), (12,13), (11,13), (11,9))
# """0 1
# 1 2
# 1 5
# 1 3
# 3 4
# 5 4
# -1"""
# """
# 0 1
# 1 5
# 5 4
# 4 3
# 3 1
# 1 2
# """
# 3
# 6 7
# 0 1 6
# 1 2 5
# 0 2 6
# 2 3 8
# 3 5 4
# 4 5 1
# 3 4 7
# 5 4
# 0 3 8
# 2 4 9
# 3 2 5
# 4 1 1
# 3 3 
# 0 1 1
# 1 2 1
# 2 0 1