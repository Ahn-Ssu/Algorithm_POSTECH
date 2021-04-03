import sys
sys.setrecursionlimit(10000)


class AdjNode:
    def __init__(self, V_id):
        self.id = V_id
        self.next = None

class Vertex:
    def __init__(self, id,  visited=False, dist=sys.maxsize):
        self.dist = dist
        self.visited = visited
        self.id = id
        self.next = None

class Graph:
    def __init__(self, num):
        self.V_num = num
        self.Adj = [None] * self.V_num
        self.VertexList = [None] * self.V_num
        
    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.Adj[s]
        self.Adj[s] = node
        

        node = AdjNode(s)
        node.next = self.Adj[d]
        self.Adj[d] = node

    # Print the graph
    def print_Adj(self):
        for i in range(self.V_num):
            print("Vertex [" + str(i) + "] :", end="")
            temp = self.Adj[i]
            while temp:
                print(" -> {}".format(temp.id), end="")
                temp = temp.next
            print()



def DFS(G):
    global s_len
    
    for idx in range(G.V_num): # visited false init
        G.VertexList[idx] = Vertex(id=idx, visited= False)
    
    for node in G.VertexList:

        if not node.visited:
            path = (node.id,)
            explore(G, node, path)

            if s_len == 3:
                return

            
            
            


def explore(G, vertex, path):
    global s_len
    # print()
    # print("in vertex id : ", vertex.id)
    # print("in now path : ", path)
    vertex.visited = True
    temp = G.Adj[vertex.id]

    while temp:
        # print("temp id :", temp.id)
        # print("now path : ", path)

        if not G.VertexList[temp.id].visited:
            # print("not visited :", temp.id)
        
            tempPath = path + (temp.id,)
            result = explore(G, G.VertexList[temp.id], tempPath)
            # print("t id : ", temp.id ,"end explore result :", result)

            if s_len == 3 :
                return 


        else: 
            if len(path) < 3:
                pass
            elif path[-1] == temp.id:
                pass
            else :
                startPoint = -1
                if temp.id in path:
                    startPoint = path.index(temp.id)
                # print("sP", startPoint)
                if startPoint != -1:
                    find_len = len(path[startPoint:])
                    if find_len > 2:
                        # print("*******")
                        # print("find id", temp.id)
                        # print("find path", path)
                        # print("find length :", len(path[startPoint:]))
                        # print("*******")

                        if s_len > find_len:
                            s_len = find_len    
                        
                        return 

        # print("temp change : ", temp.id,  end="")
        temp = temp.next
        # if temp:
        #     print(" ->",temp.id)
        # else:
        #     print("-> null")
    
    # print("explore close")
    return     



# 엣지를 전달 받으면 링크드 리스트로 제작

# node_num = 8
# edge_num = 3







stage = int(sys.stdin.readline())
output = ""

for iteration in range(stage): # 입력한 테스트 케이스 iteration 


    node_num, edge_num = tuple(map(int,sys.stdin.readline().split()))
    if edge_num < 3 :
        output += "-1\n"
        for idx in range(edge_num):
            sys.stdin.readline()
    else :
        graph = Graph(node_num)
        s_len = sys.maxsize
        E = [0] * edge_num
        
        for idx in range(edge_num):
            E[idx] = tuple(map(int,sys.stdin.readline().split()))
        # E = ((0,1), (1,4), (4,5), (5,2), (2,0), (2,3), (3,6), (6,9), (9,8), (8,10), (10,7), (10,12), (12,13), (11,13), (11,9))
        for u, v in E:
            graph.add_edge(u,v)
            

        # graph.print_Adj()
        DFS(graph)
        if s_len == sys.maxsize:
            s_len = -1
        output += "%s\n"%s_len
        

print(output)

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