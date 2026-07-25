def ucs(graph, start, goal):
    queue = [(start, 0)]
    visited = []

    while queue:

        # Find node with minimum cost
        min_index = 0
        for i in range(len(queue)):
            if queue[i][1] < queue[min_index][1]:
                min_index = i

        node, cost = queue.pop(min_index)

        if node in visited:
            continue

        visited.append(node)

        # Goal Test
        if node == goal:
            print("Minimum Cost to reach", goal, "is", cost)
            return

        # Expand neighbours
        for neighbour, weight in graph[node]:
            queue.append((neighbour, cost + weight))


# -------- Graph 1 --------
graph1 = {
    'P': [('Q', 2), ('R', 5)],
    'Q': [('S', 4)],
    'R': [('S', 1), ('T', 6)],
    'S': [('T', 2)],
    'X': [('P', 3), ('T', 10)],
    'T': []
}

# -------- Graph 2 --------
graph2 = {
    'N1': [('N2', 3), ('N3', 2)],
    'N2': [('N4', 4), ('N5', 5)],
    'N3': [('N6', 3)],
    'N4': [('N7', 2)],
    'N5': [('N8', 6)],
    'N6': [('N8', 2)],
    'N7': [],
    'N8': []
}

# -------- Graph 3 --------
graph3 = {
    'A1': [('A2', 5), ('A3', 2)],
    'A2': [('A4', 3)],
    'A3': [('A4', 2), ('A5', 7)],
    'A4': [('A6', 4)],
    'A5': [('A6', 1)],
    'A6': []
}

# -------- Graph 4 --------
graph4 = {
    'Start': [('B', 4), ('C', 3)],
    'B': [('D', 5), ('End', 12)],
    'C': [('E', 2)],
    'D': [('End', 3)],
    'E': [('End', 4)],
    'End': []
}


ucs(graph1, 'X', 'T')
print()

ucs(graph2, 'N1', 'N8')
print()

ucs(graph3, 'A1', 'A6')
print()

ucs(graph4, 'Start', 'End')
print()
