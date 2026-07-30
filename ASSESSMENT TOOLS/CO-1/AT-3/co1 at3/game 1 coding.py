from collections import deque

maze = [
    ['S',0,1,0],
    [1,0,1,0],
    [0,0,0,0],
    [1,1,0,'G']
]

rows = len(maze)
cols = len(maze[0])

queue = deque([(0,0,0)])
visited = {(0,0)}

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    x,y,steps = queue.popleft()

    if maze[x][y] == 'G':
        print("Shortest Steps =", steps)
        break

    for dx,dy in directions:
        nx,ny = x+dx,y+dy

        if 0<=nx<rows and 0<=ny<cols:
            if (nx,ny) not in visited and maze[nx][ny]!=1:
                visited.add((nx,ny))
                queue.append((nx,ny,steps+1))
