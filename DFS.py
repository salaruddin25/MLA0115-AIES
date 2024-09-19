def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start_node)
    print(start_node, end=" ")
    
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("DFS Traversal starting from node A:")
    dfs(graph, 'A')
