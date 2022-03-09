from collections import deque
import sys

max_days = -1
M,N = map(int,sys.stdin.readline().split())
board = []
tomato_queue = deque()
result = 0

# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 1 0 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
            
def bfs():
    while tomato_queue:
        a,b = tomato_queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                tomato_queue.append((nx,ny))
                board[nx][ny] = board[a][b] + 1

for x in range(N):
    for y in range(M):
        if board[x][y] == 1:
            tomato_queue.append((x,y))


bfs()

# for a in board:
#     for i in a:
#         print(i,end=" ")
#     print()

for t_array in board:
    if max(t_array) > max_days:
        max_days = max(t_array)
    for tomato in t_array:
        if tomato == 0:
            result = -1
            print(result)
            break
    if result == -1:
        break

if result != -1:
    print(max_days-1)
    
        