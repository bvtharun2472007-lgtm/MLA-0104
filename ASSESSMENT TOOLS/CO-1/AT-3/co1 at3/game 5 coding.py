from collections import deque

goal = (1,2,3,4,5,6,7,8,0)
start = (1,2,3,4,5,6,0,7,8)

moves = {
0:[1,3],
1:[0,2,4],
2:[1,5],
3:[0,4,6],
4:[1,3,5,7],
5:[2,4,8],
6:[3,7],
7:[4,6,8],
8:[5,7]
}

queue = deque([(start,0)])
visited = {start}

while queue:
    state,steps = queue.popleft()

    if state==goal:
        print("Solved in",steps,"moves")
        break

    zero = state.index(0)

    for m in moves[zero]:
        new = list(state)
        new[zero],new[m] = new[m],new[zero]
        new = tuple(new)

        if new not in visited:
            visited.add(new)
            queue.append((new,steps+1))
