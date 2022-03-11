import sys
from collections import deque

sys.setrecursionlimit(3000)

M,N,K = map(int,sys.stdin.readline().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0
result = []
board = [[1]*N for _ in range(M)]
visited = [[0]*N for _ in range(M)]
area = 0

for _ in range(K):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            board[i][j] = 0

def bfs(x,y):
    global area
    rec_queue = deque()
    rec_queue.append((x,y))
    visited[x][y] = 1
    board[x][y] = count
    area += 1
    while rec_queue:
        a,b = rec_queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    bfs(nx,ny)

for x in range(M):
    for y in range(N):
        if board[x][y] == 1 and visited[x][y] == 0:
            count += 1
            bfs(x,y)
            result.append(area)
            area = 0


for a in board:
    for j in a:
        print(j,end=" ")
    print()

print(len(result))
result.sort()
for a in result:
    print(a,end=" ")