from collections import deque

capacity = (11,9)
goal = 8

visited = set()
queue = deque([((0,0),[])])

while queue:
    (a,b),path = queue.popleft()

    if a==goal or b==goal:
        print("Solution:")
        for p in path:
            print(p)
        print("Final State:",(a,b))
        break

    if (a,b) in visited:
        continue

    visited.add((a,b))

    next_states = [
        ((11,b),"Fill 11L"),
        ((a,9),"Fill 9L"),
        ((0,b),"Empty 11L"),
        ((a,0),"Empty 9L"),
        ((a-min(a,9-b),b+min(a,9-b)),"11 -> 9"),
        ((a+min(b,11-a),b-min(b,11-a)),"9 -> 11")
    ]

    for state,action in next_states:
        if state not in visited:
            queue.append((state,path+[action]))
