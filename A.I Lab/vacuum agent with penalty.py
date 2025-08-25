import random

class Environment:
    def __init__(self):
        self.rooms = {'A': random.choice(['Clean', 'Dirty']),
                      'B': random.choice(['Clean', 'Dirty'])}
        self.agent_location = random.choice(['A', 'B'])

    def is_dirty(self, location):
        return self.rooms[location] == 'Dirty'

    def clean(self, location):
        self.rooms[location] = 'Clean'

    def move(self, new_location):
        self.agent_location = new_location

    def randomly_dirty_rooms(self, probability=0.3):
        for room in self.rooms:
            if self.rooms[room] == 'Clean' and random.random() < probability:
                self.rooms[room] = 'Dirty'
                print(f"Environment: Room {room} got dirty again!")

    def display(self):
        print(f"Agent is in room {self.agent_location}")
        print(f"Room A: {self.rooms['A']}, Room B: {self.rooms['B']}")

class ReflexVacuumAgent:
    def __init__(self):
        self.penalty = 0

    def act(self, env: Environment):
        location = env.agent_location
        
        # Check if both rooms are already clean before acting
        both_clean = all(status == 'Clean' for status in env.rooms.values())

        if env.is_dirty(location):
            print(f"Action: Suck dirt in Room {location}")
            env.clean(location)
        elif location == 'A':
            print("Action: Move Right to Room B")
            env.move('B')
            if both_clean:  # Unnecessary movement
                self.penalty -= 1
                print("Penalty: -1 (Unnecessary movement)")
        else:
            print("Action: Move Left to Room A")
            env.move('A')
            if both_clean:  # Unnecessary movement
                self.penalty -= 1
                print("Penalty: -1 (Unnecessary movement)")

# Simulation
env = Environment()
agent = ReflexVacuumAgent()

for step in range(10):
    print(f"\nStep {step + 1}")
    env.display()
    agent.act(env)
    env.randomly_dirty_rooms(probability=0.3)

# Final penalty count
print(f"\nTotal penalty after execution: {agent.penalty}")
