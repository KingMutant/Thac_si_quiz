import numpy as np
from collections import deque
import heapq


def BFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO:

    visited = {}
    queue = deque([start])
    path = []
    visited[start] = start
    while queue:
        current_node = queue.popleft()
        if current_node == end:
            path = [end]
            while start not in path:
                path.append(visited[path[-1]])
            path.reverse()
            break

        neighbors = [i for i, weight in enumerate(matrix[current_node]) if weight != 0 and i not in visited]
        for neighbor in neighbors:
            visited[neighbor] = current_node
            queue.append(neighbor)
    return visited, path


def DFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    visited = {}
    path = []
    visited[start] = start
    def recursive_dfs(node):
        nonlocal visited, path


        if node == end:
            path = [end]
            while start not in path:
                path.append(visited[path[-1]])
            path.reverse()
            return True

        neighbors = [i for i, weight in enumerate(matrix[node]) if weight != 0 and i not in visited]
        for neighbor in neighbors:
            visited[neighbor] = node
            if recursive_dfs(neighbor):
                return True

        return False

    recursive_dfs(start)

    return visited, path


def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
    Parameters:
    ---------------------------
    matrix: np array
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    path = []
    visited = {}
    priority_queue = [(0, start, start)]  # Priority queue using heapq

    while priority_queue:
        sorted_priority_queue = sorted(priority_queue, key=lambda x: x[0])

        print("Sorted Priority Queue:", sorted_priority_queue)
        cost, current_node, previous = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited[current_node] = previous

        if current_node == end:
            path = [end]
            while start not in path:
                path.append(visited[path[-1]])
            path.reverse()
            break

        for next_node, weight in enumerate(matrix[current_node]):
            if weight != 0:
                heapq.heappush(priority_queue, (cost + weight, next_node, current_node))

    return visited, path


def IDS(matrix, start, goal):
    """
    Iterative Deepening Search algorithm
    Parameters:
    ---------------------------
    matrix: np array
        The graph's adjacency matrix
    start: integer
        starting node
    goal: integer
        ending node

    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node,
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    depth_limit = 0

    while True:
        visited = {}
        path = dfs(matrix, start, goal, visited, depth_limit)

        if path:
            return visited, path

        depth_limit += 1


def dfs(matrix, current, goal, visited, depth_limit):
    """
    Depth-First Search (DFS) with depth limit
    """
    if depth_limit < 0:
        return None

    if current == goal:
        return [goal]

    visited[current] = None

    for next_node, weight in enumerate(matrix[current]):
        if weight != 0 and next_node not in visited:
            path = dfs(matrix, next_node, goal, visited, depth_limit - 1)
            if path is not None:
                visited[current] = next_node
                return [current] + path

    return None

def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
    heuristic: edge weights
    Parameters:
    ---------------------------
    matrix: np array
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node

    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node,
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    path = []
    visited = {}
    priority_queue = [(heuristic_greedy(matrix, start, end), start, start)]  # Priority queue using heapq

    while priority_queue:
        sorted_priority_queue = sorted(priority_queue, key=lambda x: x[0])
        print("priority_queue ", sorted_priority_queue)
        _, current_node, previous = heapq.heappop(sorted_priority_queue)
        print("priority_queue ", sorted_priority_queue)

        if current_node in visited:
            continue

        visited[current_node] = previous

        if current_node == end:
            path = [end]
            while start not in path:
                path.append(visited[path[-1]])
            path.reverse()
            break

        for next_node, weight in enumerate(matrix[current_node]):
            if weight != 0 and next_node not in visited:
                heapq.heappush(priority_queue, (heuristic_greedy(matrix, next_node, end), next_node, current_node))

    return visited, path


def heuristic_greedy(matrix, node, goal):
    return matrix[node][goal]


def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
    heuristic: eclid distance based positions parameter
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 

    def heuristic_astar(current_vertex, goal, position):
        distance = np.sqrt((position[current_vertex][0] - position[goal][0]) ** 2 + (position[current_vertex][1] - position[goal][1]) ** 2)
        return distance

    priority_queue = [(0, start, start)]
    g_values = {node: float('inf') for node in range(len(matrix))}
    g_values[start] = 0

    visited = {}
    path = []

    while priority_queue:
        priority_queue = sorted(priority_queue, key=lambda x: x[0])
        _, current_node, previous = heapq.heappop(priority_queue)
        if current_node in visited:
            continue

        visited[current_node] = previous

        if current_node == end:
            path = [end]
            while start not in path:
                path.append(visited[path[-1]])
            path.reverse()
            break

        for next_node, weight in enumerate(matrix[current_node]):
            if weight != 0:
                g = g_values[current_node] + weight
                h = heuristic_astar(next_node, end, pos)
                f = g + h

                if g < g_values[next_node]:
                    g_values[next_node] = g
                    print("Sorted g Value:", g_values)
                    heapq.heappush(priority_queue, (f, next_node, current_node))

    return visited, path

