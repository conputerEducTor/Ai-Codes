
num_nodes = int(input("enter no of nodes: "))
num_edges = int(input("how many edges?: "))
edges = [tuple(map(int, input("enter edge: ").split())) for r in range(num_edges)]


class Graph:
    def __init__(self, num_nodes, edges):
        self.data = [[] for _ in range(num_nodes)]
        for v1, v2 in edges:
            for edge in edges:
                self.data[v1].append(v2)
                self.data[v2].append(v1)
        self.data = [list(set(entry)) for entry in self.data]

    def __repr__(self):
        return "\n".join(["{} : {}".format(i, neighbors) for (i, neighbors) in enumerate(self.data)])

    def __str__(self):
        return repr(self)

g1 = Graph(num_nodes, edges)



while True:
    print("Enter\n1.Display Graph 2.BFS  3.DFS 4.Quit:  ")
    user = int(input());

   
    if user == 1:
        print(g1)

    
    elif user == 2:
        source = int(input("Enter the source for bfs:"))
        def bfs(graph, source):
            visited = [False] * len(graph.data)
            queue = []
            visited[source] = True
            queue.append(source)
            i = 0
            while i < len(queue):
                for v in graph.data[queue[i]]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
                i += 1
            return queue
        print(bfs(g1,source ))

  
    elif user == 3:
        source1 =int(input("Enter the source for dfs:"))

        def dfs(graph, source):
            visited = [False] * len(graph.data)
            stack = [source]
            result = []
            while len(stack) > 0:
                current = stack.pop()
                if not visited[current]:
                    result.append(current)
                    visited[current] = True
                    for v in graph.data[current]:
                        stack.append(v)

            return result
        print(dfs(g1,source1))

    
    elif user == 4:
        break
    
    else:
        print("Please choose correct Option !!!")














