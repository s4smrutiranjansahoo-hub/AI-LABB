def dfs(graph, current_node, visited):
    if current_node not in visited:
        print(f"Exploring node: {current_node}")
        visited.append(current_node)

        for neighbour in graph.get(current_node, []):
            dfs(graph, neighbour, visited)

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
start = input("Enter your starting node for DFS: ")

print("\nYour Graph Dictionary:", student_graph)
print("Starting DFS Traversal...")

visited_nodes = dfs(student_graph, start, [])

print("DFS Traversal:", visited_nodes)
