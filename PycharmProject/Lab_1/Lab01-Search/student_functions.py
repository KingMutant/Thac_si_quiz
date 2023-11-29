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

    while queue:
        current_node = queue.popleft()
        print(f"Processing node: {current_node}")
        print("Queue:", list(queue))
        print("Visited nodes:", visited)
        print("Current path:", path)

        visited[current_node] = True

        if current_node == end:
            path = [end]
            while start not in path:
                path.append(visited[path[-1]])
            path.reverse()
            print("Path found:", path)
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

    path = []
    visited = {}

    def recursive_dfs(node):
        nonlocal visited, path

        print(f"Processing node: {node}")
        print("Visited nodes:", visited)
        print("Current path:", path)

        visited[node] = True

        if node == end:
            path = [end]
            while start not in path:
                path.append(visited[path[-1]])
            path.reverse()
            print("Path found:", path)
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
    priority_queue = [(0, start)]  # Priority queue using heapq

    while priority_queue:
        heapq._heapify_max(priority_queue)
        priority_queue.reverse()
        print("Priority Queue:", priority_queue)
        cost, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited[current_node] = True

        if current_node == end:
            path = [end]
            while start not in path:
                path.append(visited[path[-1]])
            path.reverse()
            print("Path found:", path)
            break

        for next_node, weight in enumerate(matrix[current_node]):
            if weight != 0:
                heapq.heappush(priority_queue, (cost + weight, next_node))

    print("Visited:", visited)
    print("Path found:", path)
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
        visited, path = depth_limited_DFS(matrix, start, goal, depth_limit)
        if goal in visited:
            return visited, path
        depth_limit += 1


def depth_limited_DFS(matrix, start, goal, depth_limit):
    """
    Depth-Limited DFS for IDS
    """
    path = []
    visited = {}
    stack = [(start, 0)]  # Using a stack to implement DFS with depth limit

    while stack:
        current_node, depth = stack.pop()

        if current_node in visited and visited[current_node] <= depth:
            continue

        visited[current_node] = depth
        path.append(current_node)

        if current_node == goal:
            return visited, path

        if depth < depth_limit:
            neighbors = [i for i, value in enumerate(matrix[current_node]) if value != 0]
            for neighbor in neighbors:
                stack.append((neighbor, depth + 1))

    return visited, path


def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm 
    heuristic : edge weights
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
    path = []
    visited = {}
    return visited, path


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

    path = []
    visited = {}
    return visited, path
