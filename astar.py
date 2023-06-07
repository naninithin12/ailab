from queue import PriorityQueue

def astar(graph, start, goal, heuristic):
    # Initialize data structures
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while not open_set.empty():
        # Get node with the lowest f_score
        current_cost, current_node = open_set.get()

        if current_node == goal:
            # Reconstruct path
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path

        for neighbor in graph[current_node]:
            # Calculate tentative g_score
            tentative_g_score = g_score[current_node] + graph[current_node][neighbor]
            if tentative_g_score < g_score[neighbor]:
                # Update g_score and add to open set
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                open_set.put((f_score, neighbor))
                came_from[neighbor] = current_node

    return None  # No path found
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2,'C':1},
    'C': {'D': 7, 'E': 8},
    'D': {'E': 4, 'F': 6},
    'E': {'G': 9},
    'F': {'G': 3},
    'G': {}
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 6,
    'E': 4,
    'F': 3,
    'G': 0
}

start_node = 'A'
goal_node = 'C'

shortest_path = astar(graph, start_node, goal_node, heuristic)
if shortest_path:
    print("Shortest path:", shortest_path)
else:
    print("No path found.")
