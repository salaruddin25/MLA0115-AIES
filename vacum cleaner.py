class VacuumCleaner:
    def __init__(self):
        self.location = 'A'
        self.environment = {'A': 'Dirty', 'B': 'Dirty'}
        self.performance = 0

    def clean(self):
        if self.environment[self.location] == 'Dirty':
            self.environment[self.location] = 'Clean'
            self.performance += 1
            print(f"Location {self.location} is cleaned.")
        else:
            print(f"Location {self.location} is already clean.")

    def move(self):
        if self.location == 'A':
            self.location = 'B'
        else:
            self.location = 'A'
        print(f"Moved to location {self.location}.")

    def run(self):
        print("Initial Environment:", self.environment)
        print("Starting cleaning process...")
        for _ in range(2):  # Run two steps (for both rooms)
            self.clean()
            self.move()
            self.clean()
        print("Final Environment:", self.environment)
        print("Performance:", self.performance)

if __name__ == "__main__":
    agent = VacuumCleaner()
    agent.run()
