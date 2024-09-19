from heapq import heappop, heappush

# A* algorithm implementation
def a_star(graph, start, goal, h):
    open_set = []
    heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = h[start]

    while open_set:
        current = heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + h[neighbor]
                heappush(open_set, (f_score[neighbor], neighbor))

    return None

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

if __name__ == "__main__":
    # Example graph where the edges have weights (distances)
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    # Heuristic function (estimated cost to reach the goal)
    h = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 0  # 'D' is the goal
    }

    start = 'A'
    goal = 'D'
    path = a_star(graph, start, goal, h)

    print("Path found by A* algorithm:", " -> ".join(path))
