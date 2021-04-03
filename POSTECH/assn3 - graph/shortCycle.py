import sys

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
            print("Vertex " + str(i) + ":", end="")
            temp = self.Adj[i]
            while temp:
                print(" -> {}".format(temp.id), end="")
                temp = temp.next
            print()



# 엣지를 전달 받으면 링크드 리스트로 제작

node_num = 8
edge_num = 3



# ((0,1),(1,2),(0,2))
#((0,1), (1,2),(1,3),(3,2),(2,4),(4,1)) 
#((0,1),(0,2),(1,2),(1,3),(3,4),(1,4),(4,5),(2,7),(2,6)) 
#((0,1),(0,2),(1,3),(1,4),(4,5),(2,7),(2,6))
#( (0,1), (0,2), (1,3), (1,4), (2,4), (4,5))
# ( (0,1), (0,2), (1,3), (1,4), (2,4), (4,5), (2,7),(2,6),(6,7))
# ( (0,1), (1,2))
E = ( (0,1), (1,2))
print(E)




# if __name__ == "__main__":


# Create graph and edges
graph = Graph(node_num)


for v, u in E :
    graph.add_edge(v, u)

print(graph)
graph.print_Adj()

# for i in range(3):
    
#     temp = graph.Adj[i]
#     while temp:
#         print(temp.id)
#         temp = temp.nex


def DFS(G):
    result = 0 
    for idx in range(G.V_num): # visited false init
        G.VertexList[idx] = Vertex(id=idx, visited= False)
    
    for node in G.VertexList:

        if not node.visited:
            print("not visitied in DFS", node.id)
            path = str(node.id)
            result = explore(G, node, path)

            if result == 3 :
                return result

    if result:
        return result
    else :
        return -1


def explore(G, vertex, path):
    print()
    print("in vertex id : ", vertex.id)
    print("in now path : ", path)
    vertex.visited = True
    temp = G.Adj[vertex.id]
    result = 0 
    while temp:
        print("temp id :", temp.id)
        print("now path : ", path)

        if not G.VertexList[temp.id].visited:
            print("not visited :", temp.id)
        
            tempPath = path+str(temp.id)
            result = explore(G, G.VertexList[temp.id], tempPath)

            if result == 3 :
                return result


        else: 
            if len(path) < 3:
                pass
            elif int(path[-1]) == temp.id:
                pass
            else :
                startPoint = path.find(str(temp.id))
                # print("sP", startPoint)
                if startPoint != -1:
                    if len(path[startPoint:]) > 2:
                        # print("*******")
                        # print("find id", temp.id)
                        # print("find path", path)
                        # print("find length :", len(path[startPoint:]))
                        # print("*******")
                        return len(path[startPoint:])

        # print("temp change : ", temp.id,  end="")
        temp = temp.next
        # if temp:
        #     print(" ->",temp.id)
        # else:
        #     print("-> null")
    
    # print("explore close")
    return result
    
    
print("DFS result : ", DFS(graph))