from collections import deque

def bfs(graph, start_node):
    queue = deque([start_node])
    visited = set([start_node])
    
    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("BFS Traversal starting from node A:")
    bfs(graph, 'A')
