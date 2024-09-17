import heapq

# The goal state of the 8-puzzle
goal_state = [[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 0]]

# Helper function to check if the current state is the goal state
def is_goal(state):
    return state == goal_state

# Helper function to get the Manhattan distance between a tile and its goal position
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                # Calculate the goal position of the tile
                goal_x = (state[i][j] - 1) // 3
                goal_y = (state[i][j] - 1) % 3
                # Add the Manhattan distance to the total distance
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Helper function to find the blank tile's position (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Helper function to get the possible moves of the blank tile
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    
    # Possible moves: up, down, left, right
    moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    
    for new_x, new_y in moves:
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            # Create a new state by swapping the blank tile with the neighbor
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    
    return neighbors

# A* search algorithm
def a_star(initial_state):
    # Priority queue for the open set
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(initial_state), 0, initial_state, []))
    
    # Set to store visited states
    visited = set()
    
    while open_set:
        # Get the state with the lowest cost (f = g + h)
        f, g, current_state, path = heapq.heappop(open_set)
        
        # Check if the goal is reached
        if is_goal(current_state):
            return path + [current_state]
        
        # Add the current state to the visited set
        visited.add(tuple(map(tuple, current_state)))
        
        # Get the neighbors of the current state
        for neighbor in get_neighbors(current_state):
            neighbor_tuple = tuple(map(tuple, neighbor))
            
            # If the neighbor hasn't been visited, add it to the open set
            if neighbor_tuple not in visited:
                heapq.heappush(open_set, (g + 1 + manhattan_distance(neighbor), g + 1, neighbor, path + [current_state]))
    
    return None

# Helper function to print the 8-puzzle state
def print_puzzle(state):
    for row in state:
        print(row)
    print()

# Example usage
initial_state = [[1, 2, 3], 
                 [4, 0, 5], 
                 [7, 8, 6]]

solution = a_star(initial_state)

if solution:
    print("Solution found:")
    for step in solution:
        print_puzzle(step)
else:
    print("No solution exists.")
