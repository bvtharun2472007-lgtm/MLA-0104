def gbfs(graph, h, start, goal):

    open_list = [(start, [start], h[start])]
    visited = []

    while open_list:

        # Choose node with smallest heuristic value
        open_list.sort(key=lambda x: x[2])
        node, path, cost = open_list.pop(0)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Cost:", cost)
            print()
            return

        visited.append(node)

        for n in graph[node]:
            if n not in visited:
                open_list.append((n, path + [n], cost + h[n]))


# -------- Example 1 --------
print("Example 1")

graph1 = {
    'S': ['A', 'B', 'C'],
    'A': ['D'],
    'B': ['E', 'F'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['H'],
    'G': ['I'],
    'H': ['I'],
    'I': []
}

h1 = {
    'S': 15,
    'A': 12,
    'B': 8,
    'C': 10,
    'D': 7,
    'E': 5,
    'F': 4,
    'G': 3,
    'H': 2,
    'I': 0
}

gbfs(graph1, h1, 'S', 'I')


# -------- Example 2 --------
print("Example 2")

graph2 = {
    'X': ['Y', 'Z'],
    'Y': ['P', 'Q'],
    'Z': ['R'],
    'P': ['T'],
    'Q': ['T'],
    'R': ['U'],
    'T': ['V'],
    'U': ['V'],
    'V': []
}

h2 = {
    'X': 18,
    'Y': 10,
    'Z': 12,
    'P': 6,
    'Q': 5,
    'R': 4,
    'T': 2,
    'U': 3,
    'V': 0
}

gbfs(graph2, h2, 'X', 'V')
