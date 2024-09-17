class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = None

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries > 0 and self.missionaries < self.cannibals:
            return False
        if self.missionaries < 3 and (3 - self.missionaries) < (3 - self.cannibals):
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def get_successors(self):
        successors = []
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for move in moves:
            if self.boat == 1:
                new_state = State(self.missionaries - move[0], self.cannibals - move[1], 0)
            else:
                new_state = State(self.missionaries + move[0], self.cannibals + move[1], 1)

            if new_state.is_valid():
                new_state.parent = self
                successors.append(new_state)
        return successors

def bfs():
    initial_state = State(3, 3, 1)
    if initial_state.is_goal():
        return initial_state
    frontier = [initial_state]
    explored = set()
    while frontier:
        state = frontier.pop(0)
        explored.add((state.missionaries, state.cannibals, state.boat))
        for successor in state.get_successors():
            if (successor.missionaries, successor.cannibals, successor.boat) not in explored:
                if successor.is_goal():
                    return successor
                frontier.append(successor)

def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent
    path.reverse()
    for step in path:
        print(f"Missionaries: {step.missionaries}, Cannibals: {step.cannibals}, Boat: {step.boat}")

solution = bfs()
if solution:
    print_solution(solution)
else:
    print("No solution found")
