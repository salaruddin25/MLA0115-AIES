# Function to check if the current color assignment is valid
def is_valid(assignment, state, color, graph):
    for neighbor in graph[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking function to solve the CSP
def csp_backtracking(assignment, graph, colors):
    if len(assignment) == len(graph):
        return assignment  # All states have been colored successfully

    # Select an unassigned state
    unassigned_states = [state for state in graph if state not in assignment]
    state = unassigned_states[0]

    # Try different colors for the selected state
    for color in colors:
        if is_valid(assignment, state, color, graph):
            assignment[state] = color  # Assign color

            # Recursively assign colors to the remaining states
            result = csp_backtracking(assignment, graph, colors)
            if result:
                return result

            # If no solution is found, backtrack
            del assignment[state]

    return None  # No valid assignment found

if __name__ == "__main__":
    # Example graph (Map of Australia)
    graph = {
        'Western Australia': ['Northern Territory', 'South Australia'],
        'Northern Territory': ['Western Australia', 'South Australia', 'Queensland'],
        'South Australia': ['Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'],
        'Queensland': ['Northern Territory', 'South Australia', 'New South Wales'],
        'New South Wales': ['Queensland', 'South Australia', 'Victoria'],
        'Victoria': ['South Australia', 'New South Wales'],
        'Tasmania': []
    }

    # List of colors
    colors = ['Red', 'Green', 'Blue']

    # Start the CSP solver
    solution = csp_backtracking({}, graph, colors)

    if solution:
        print("Solution found:")
        for state, color in solution.items():
            print(f"{state}: {color}")
    else:
        print("No solution exists")
