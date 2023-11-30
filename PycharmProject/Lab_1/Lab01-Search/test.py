import numpy as np

def generate_heuristic(start, goal, pos):
    """
    Generate heuristic values for each node based on Euclidean distance to the goal node.
    Parameters:
    ---------------------------
    start: integer
        starting node
    goal: integer
        goal node
    pos: dictionary
        positions of graph nodes
    Returns
    ---------------------
    heuristic_values: float
        heuristic value for the given start and goal nodes
    """
    # Calculate Euclidean distance between node and goal
    distance = np.sqrt((pos[start][0] - pos[goal][0])**2 + (pos[start][1] - pos[goal][1])**2)
    return distance

# Example usage:
pos = {
    0: (0, 0),
    1: (1, 1),
    2: (2, 2),
    3: (3, 3),
    4: (4, 4),
    5: (5, 5),
    6: (6, 6),
    7: (7, 7)
}

start_node = 4
goal_node = 6

heuristic_value = generate_heuristic(start_node, goal_node, pos)
print("Heuristic Value:", heuristic_value)
