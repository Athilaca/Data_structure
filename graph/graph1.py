
class Graph:
    def __init__(self):
        self.graph = {}

    # my_dict={}
    # my_dict['key1'] = 'value1'
    # my_dict['key2'] = 42
    # my_dict['key3'] = [1, 2, 3]    

    # def add_vertex(self, vertex):
    #     if vertex not in self.graph:
    #         self.graph[vertex] = []

    # def add_edge(self, from_vertex, to_vertex):
    #     self.add_vertex(from_vertex)
    #     self.add_vertex(to_vertex)
    #     self.graph[from_vertex].append(to_vertex)
    #     self.graph[to_vertex].append(from_vertex)  # For an undirected graph

    def add_edge(self, node1, node2):
        # Adding edge in both directions for an undirected graph
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append(node2)

        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node2].append(node1)

    def display_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")    


    def remove_edge(self, node1, node2):
        # Removing edge in both directions for an undirected graph
        if node1 in self.graph and node2 in self.graph[node1]:
            self.graph[node1].remove(node2)

        if node2 in self.graph and node1 in self.graph[node2]:
            self.graph[node2].remove(node1)

    def remove_vertex(self, vertex):   
        if vertex in self.graph:
            del self.graph[vertex]
            for v in self.graph:
                self.graph[v] = [neighbor for neighbor in self.graph[v] if neighbor != vertex]

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def dfs_stack(self, start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                stack.extend(neighbor for neighbor in self.graph[node] if neighbor not in visited)


    def bfs_queue(self,start):
        visited = set()
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(neighbor for neighbor in self.graph[node] if neighbor not in visited)



# Example usage:
graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
# graph.add_vertex("E")  # Adding a single vertex

graph.display()
print("\nDFS using stack:")
graph.dfs_stack("A")
graph.bfs_queue("A")