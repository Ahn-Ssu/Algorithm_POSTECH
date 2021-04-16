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


def DFS(G):
    global min_W
    
    root = G.VertexList[0]
    rootAdj = G.Adj[root.id]

    root.visited = True
    root.idx_ = 1

    while rootAdj:
        nextNode = G.VertexList[rootAdj.id]

        if nextNode.visited == False:
            

            low = explore(G, nextNode, root) 

            if low > root.idx_ :
                # print("루트에서 바로 커트 하면 됩니다 손님!!!")
                # print("현재 위치 [{}] -- {} -- [{}]".format(root.id, rootAdj.weight, rootAdj.id))
                min_W = min(rootAdj.weight, min_W)

        rootAdj = rootAdj.next

    

def explore(G, vertex, parent):
    global find_idx, min_W
    vertex.visited = True
    
    vertex.idx_ = find_idx
    find_idx += 1

    early = vertex.idx_

    temp = G.Adj[vertex.id]
    low = -1
    while temp:

        if temp.id == parent.id : # 부모에게 바로 돌아가는 길 외에 길을 확인해야 함
            # print("저 {}에게 얘 {}는 부모노드예요. = ".format(vertex.id, parent.id))
            temp = temp.next
            continue
        
        nextNode = G.VertexList[temp.id]
        # print("parent.id {}, idx {}".format(parent.id, parent.idx_))
        # print("vertex.id {}, idx {}".format(vertex.id, vertex.idx_))
        # print("nextN  id {}, idx {}".format(nextNode.id, nextNode.idx_))

        if not nextNode.visited:
            low = explore(G, nextNode, vertex) # 서칭한 노드 중에, 제일 빨랐던 idx의 값을 리턴
            early = min(early, low)
        # else :
        #     early = min(early, nextNode.idx_)
        
        if vertex.idx_ > nextNode.idx_ : # 상위 노드를 만남 
            # print("상위 노드 만났어요. 지금 노드는 {}/{} 이고, 만난 노드는 {}/{}예요".format(vertex.id, vertex.idx_, nextNode.id, nextNode.idx_))
            early = min(early, nextNode.idx_ )

        if low > vertex.idx_:
            # print("아래 검색에서 저쪽으로 밖에 길이 없다고 결과가 나왔습니다!")
            # print("현재 위치 [{}] -- {} -- [{}]".format(vertex.id, temp.weight, temp.id))
            min_W = min(temp.weight, min_W)
        

        temp = temp.next

    # if low == vertex.idx_:
        # print("여기서 커트 해야 합니당!")

    
    
    # print("현재 vertex {}/{} 노드에서 보았습니다. 리턴할 early값은 {}예요".format(vertex.id,vertex.idx_,early))
    # if vertex.id == 3 :
    #     input()
    return early



stage = int(sys.stdin.readline())
output = ""

for iteration in range(stage): # 입력한 테스트 케이스 iteration 
    find_idx = 1
    min_W = sys.maxsize

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
        

    # graph.print_Adj()
    DFS(graph)

    # for node in graph.VertexList:
    #     print("id : {}, visit idx_ : {}".format(node.id, node.idx_))
    if min_W == sys.maxsize:
        output += "-1\n"
    else:
        output += "%s\n"%min_W
        

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