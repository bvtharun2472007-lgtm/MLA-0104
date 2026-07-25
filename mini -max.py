def minimax(depth, nodeIndex, isMax, values, height):
    # Base case: reach leaf node
    if depth == height:
        return values[nodeIndex]

    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, height)
        )

# Changed leaf node values
values = [9, 5, 2, 8, 7, 4, 6, 3]

# Height of binary tree
height = 3

result = minimax(0, 0, True, values, height)

print("Optimal value using Mini-Max:", result)
