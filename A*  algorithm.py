import heapq

def a_star(graph, heuristic, start, goal):
    # Priority queue: (f_score, node)
    open_list = [(heuristic[start], start)]

    # Cost from start node to each node
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    # Stores the parent of each node
    parent = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path, g_score[goal]

        # Explore neighboring nodes
        for neighbor, cost in graph[current]:
            tentative_g = g_score[current] + cost

            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                parent[neighbor] = current

                # f(n) = g(n) + h(n)
                f_score = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))

    return None, float('inf')


# Graph represented as adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

# Heuristic values h(n)
heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

# Start and goal nodes
start = 'A'
goal = 'D'

path, cost = a_star(graph, heuristic, start, goal)

if path:
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")
