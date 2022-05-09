import sys
from collections import deque

sys.setrecursionlimit(1000000)

n,m = map(int,sys.stdin.readline().split())
visited = [[False]*m for _ in range(n)]
board = []
drawing_number = 0
drawing_area = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
area = 0

for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

def bfs(x,y):
    global area
    root = deque()
    root.append((x,y))
    visited[x][y] = True
    area += 1
    
    while root:
        a,b = root.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    root.append((nx,ny))
                    area += 1

for x in range(n):
    for y in range(m):
        if board[x][y] != 0 and not visited[x][y]:
            bfs(x,y)
            drawing_number += 1
            drawing_area.append(area)
            area = 0

print(drawing_number)
if drawing_area:
    print(max(drawing_area))
else:
    print(0)

# for a in board:
#     print(a)

# for a in visited:
#     print(a)