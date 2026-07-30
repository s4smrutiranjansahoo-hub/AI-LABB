def bfs(graph, start_node):
    visited = []
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)

        if current_node not in visited:
            print(f"Exploring node: {current_node}")
            visited.append(current_node)

            # .get() prevents an error if a node has no outgoing edges
            for neighbour in graph.get(current_node, []):
                if neighbour not in visited and neighbour not in queue:
                    queue.append(neighbour)

    return visited


# ----- User Input Section -----
print("----- Build Your Graph -----")

student_graph = {}

# Get the total number of edges
num_edges = int(input("How many edges (connections) does your graph have? "))

print("Enter each edge separated by a space (e.g., A B):")

for i in range(num_edges):
    u, v = input(f"Edge {i+1}: ").split()

    # Initialize lists if nodes don't exist
    if u not in student_graph:
        student_graph[u] = []
    if v not in student_graph:
        student_graph[v] = []

    # Add connection (Undirected Graph)
    student_graph[u].append(v)
    student_graph[v].append(u)

# Get the starting node
start = input("Enter your starting node for BFS: ")

print("\nYour Graph Dictionary:", student_graph)
print("Starting BFS Traversal...")

visited_nodes = bfs(student_graph, start)

print("BFS Traversal:", visited_nodes)
