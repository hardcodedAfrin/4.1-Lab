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

class PredictiveVacuumAgent:
    def __init__(self):
        self.clean_counter = {'A': 0, 'B': 0}  # How many steps each room stayed clean

    def act(self, env: Environment):
        location = env.agent_location
        other_location = 'B' if location == 'A' else 'A'

        # Update clean counters
        for room in env.rooms:
            if env.rooms[room] == 'Clean':
                self.clean_counter[room] += 1
            else:
                self.clean_counter[room] = 0  # reset if dirty

        # If current room dirty → clean
        if env.is_dirty(location):
            print(f"Action: Suck dirt in Room {location}")
            env.clean(location)

        # If both rooms clean → stay until prediction says move
        elif env.rooms['A'] == 'Clean' and env.rooms['B'] == 'Clean':
            # Prediction: move if other room has been clean for too long
            if self.clean_counter[other_location] >= 3:  # 3 steps without dirt
                print(f"Prediction: Room {other_location} might get dirty soon. Moving there.")
                env.move(other_location)
            else:
                print("Action: Stay in place (both rooms clean, low dirt probability)")
        
        # If current room clean but other is dirty → move
        elif env.is_dirty(other_location):
            print(f"Action: Move to Room {other_location} to clean")
            env.move(other_location)
        else:
            print("Action: Stay in place (no dirt)")

# Run simulation
env = Environment()
agent = PredictiveVacuumAgent()

for step in range(10):
    print(f"\nStep {step + 1}")
    env.display()
    agent.act(env)
    env.randomly_dirty_rooms(probability=0.3)

'''
model based agent, predicts the appearance of being clean any room keeping the count of being clean,
stops moving when both room is clean to restrict unnecessary movement.
again moves when predicting of being dirty again

'''