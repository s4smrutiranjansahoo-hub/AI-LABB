# DT : 1/10/26
# EXP 8 : WATER JUG PROBLEM

from collections import deque

# Function to solve Water Jug Problem using BFS
def water_jug(capacity1, capacity2, target):

    visited = set()
    queue = deque()

    # Initial state: both jugs are empty
    queue.append((0, 0, []))

    while queue:

        jug1, jug2, path = queue.popleft()

        # Skip if state is already visited
        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        # Add current state to path
        path = path + [(jug1, jug2)]

        # Check if target is reached
        if jug1 == target or jug2 == target:
            return path

        # Generate possible next states
        next_states = [

            # Fill Jug 1
            (capacity1, jug2),

            # Fill Jug 2
            (jug1, capacity2),

            # Empty Jug 1
            (0, jug2),

            # Empty Jug 2
            (jug1, 0),

            # Pour Jug 1 -> Jug 2
            (
                jug1 - min(jug1, capacity2 - jug2),
                jug2 + min(jug1, capacity2 - jug2)
            ),

            # Pour Jug 2 -> Jug 1
            (
                jug1 + min(jug2, capacity1 - jug1),
                jug2 - min(jug2, capacity1 - jug1)
            )
        ]

        # Add new states to queue
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    # No solution found
    return None


# Main program

jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

solution = water_jug(jug1, jug2, target)

if solution:
    print("\nSteps to reach the target:")

    for step in solution:
        print(step)

else:
    print("No solution exists.")
