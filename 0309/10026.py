import sys
from collections import deque

count = 0
count2 = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input())
board = []
board_abnormal = [[0]*N for _ in range(N)]
for _ in range(N):
    board.append(list(input()))
    
visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        board_abnormal[i][j] = board[i][j]
        
for i in range(N):
    for j in range(N):
        if board_abnormal[i][j] == 'G':
            board_abnormal[i][j] = 'R'


def bfs(x,y):
    color_queue = deque()
    color_queue.append((x,y))
    word = board[x][y]
    board[x][y] = count
    visited[x][y] = 1
    while color_queue:
        a,b = color_queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == word and visited[nx][ny] == 0:
                board[nx][ny] = count
                visited[nx][ny] = 1
                color_queue.append((nx,ny))

def bfs2(x,y):
    color_queue = deque()
    color_queue.append((x,y))
    word = board_abnormal[x][y]
    board_abnormal[x][y] = count2
    visited[x][y] = 1
    while color_queue:
        a,b = color_queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board_abnormal[nx][ny] == word and visited[nx][ny] == 0:
                board_abnormal[nx][ny] = count2
                visited[nx][ny] = 1
                color_queue.append((nx,ny))

for x in range(N):
    for y in range(N):
        if visited[x][y] == 0:
            bfs(x,y)
            count += 1

visited = [[0]*N for _ in range(N)]

for x in range(N):
    for y in range(N):
        if visited[x][y] == 0:
            bfs2(x,y)
            count2 += 1

print(count,count2)
