# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 1, 'D': 5},
#     'C': {'A': 4, 'B': 1, 'D': 3},
#     'D': {'B': 5, 'C': 3, 'E': 8, 'F': 3, 'G': 9},
#     'E': {'D': 8, 'G': 2},
#     'F': {'D': 3, 'G': 5},
#     'G': {'D': 9, 'E': 2, 'F': 5}
# }
#
#
# def dfs(graph, start, goal):
#     stack = [(start, [start])]
#     visited = set()
#
#     while stack:
#         current, path = stack.pop()
#
#         if current == goal:
#             return path, visited
#
#         if current not in visited:
#             visited.add(current)
#             neighbors = graph[current]
#             for neighbor, cost in sorted(neighbors.items(), key=lambda x: x[1], reverse=True):
#                 stack.append((neighbor, path + [neighbor]))
#
#         print(f"Stack at Step {len(visited)}: {stack}")
#
#     return None, visited
#
#
# # Start and Goal nodes
# start_node = 'A'
# goal_node = 'G'
#
# # Perform DFS
# result_path, visited_states = dfs(graph, start_node, goal_node)
#
# # Display the transformation steps of the stack and visited states
# for i, (node, visited) in enumerate(zip(result_path, visited_states)):
#     print(f"Step {i + 1}: Stack = {result_path[:i + 1]}, Visited = {visited}")
#
# print(f"Optimal Path: {result_path}")

import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 1, 'D': 5},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'B': 5, 'C': 3, 'E': 8, 'F': 3, 'G': 9},
    'E': {'D': 8, 'G': 2},
    'F': {'D': 3, 'G': 5},
    'G': {'D': 9, 'E': 2, 'F': 5}
}


def ucs(graph, start, goal):
    fringe = [(0, start, [start])]
    visited = set()

    while fringe:
        cost, current, path = heapq.heappop(fringe)

        if current == goal:
            return path, visited

        if current not in visited:
            visited.add(current)
            neighbors = graph[current]
            for neighbor, edge_cost in neighbors.items():
                heapq.heappush(fringe, (cost + edge_cost, neighbor, path + [neighbor]))

        print(f"Fringe at Step {len(visited)}: {fringe}")

    return None, visited


# Start and Goal nodes
start_node = 'A'
goal_node = 'G'

# Perform UCS
result_path, visited_states = ucs(graph, start_node, goal_node)

# Display the transformation steps of the fringe and visited states
for i, (node, visited) in enumerate(zip(result_path, visited_states)):
    print(f"Step {i + 1}: Fringe = {result_path[:i + 1]}, Visited = {visited}")

print(f"Optimal Path: {result_path}")