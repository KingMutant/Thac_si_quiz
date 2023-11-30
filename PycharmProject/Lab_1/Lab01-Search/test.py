import numpy as np


def generate_heuristic(pos, goal_node):
    """
    Generate heuristic function h based on Euclidean distance.
    Parameters:
    ---------------------------
    pos: dict
        Dictionary containing node positions. Keys are node indices, and values are positions.
    goal_node: int
        The goal node index.

    Returns:
    ---------------------
    h: dict
        Dictionary containing heuristic values for each node.
    """
    h = {}
    goal_position = pos[goal_node]

    for node, position in pos.items():
        x1, y1 = position
        x2, y2 = goal_position
        euclidean_distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        h[node] = euclidean_distance

    return h


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

goal_node = 6

heuristic_values = generate_heuristic(pos, goal_node)
print("Heuristic Values:", heuristic_values)