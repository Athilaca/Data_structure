class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.graph[from_vertex].append(to_vertex)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

# Example usage:
directed_graph = DirectedGraph()
directed_graph.add_edge("A", "B")
directed_graph.add_edge("A", "C")
directed_graph.add_edge("B", "C")
directed_graph.add_edge("C", "D")
directed_graph.add_vertex("E")  # Adding a single vertex

directed_graph.display()
