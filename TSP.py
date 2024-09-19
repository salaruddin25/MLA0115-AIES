from itertools import permutations

def calculate_distance(graph, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i+1]]
    total_distance += graph[path[-1]][path[0]]  # Return to the starting city
    return total_distance

def tsp(graph):
    cities = list(graph.keys())
    all_permutations = permutations(cities)
    min_distance = float('inf')
    best_path = None

    for perm in all_permutations:
        current_distance = calculate_distance(graph, perm)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = perm

    return best_path, min_distance

if __name__ == "__main__":
    # Example graph: adjacency matrix where graph[i][j] represents the distance between city i and city j
    graph = {
        'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
    }

    best_path, min_distance = tsp(graph)
    print("Best path:", " -> ".join(best_path))
    print("Minimum distance:", min_distance)
