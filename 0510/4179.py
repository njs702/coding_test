import queue
import sys
from collections import deque

board = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

R,C = map(int,sys.stdin.readline().split())
for _ in range(R):
    board.append(list(sys.stdin.readline().rstrip()))

dist_fire = [[-1]*C for _ in range(R)]
dist_jihoon = [[-1]*C for _ in range(R)]
queue_jihoon = deque()
queue_fire = deque()

# 지훈이 위치를 처리할 queue와 불을 처리할 queue에 각각 현재 맞는 좌표를
# 넣어준다
for x in range(R):
    for y in range(C):
        if board[x][y] == 'J':
            queue_jihoon.append((x,y))
            dist_jihoon[x][y] = 0
        if board[x][y] == 'F':
            queue_fire.append((x,y))
            dist_fire[x][y] = 0

# 불에 대한 BFS 먼저 실행
while queue_fire:
    a,b = queue_fire.popleft()
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        
        # 불은 단순히 '.' 인 부분으로 퍼져나가면 된다.
        if 0 <= nx < R and 0 <= ny < C:
            if dist_fire[nx][ny] < 0 and board[nx][ny] != '#':
                dist_fire[nx][ny] = dist_fire[a][b] + 1
                queue_fire.append((nx,ny))

# 지훈이 위치에 대한 BFS 실행
# 지훈이가 갈 수 있는곳 : 1. 범위 내에서 2. 방문하지 않았고 벽이 아니고 
# 3. 방문하려는 곳이 불이 번지지 않았거나(or) 지훈이가 이동할 경우 걸리는 시간 < 불이 번진 시간일 경우에만 이동 가능

while queue_jihoon:
    a,b = queue_jihoon.popleft()
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        
        # 1. 범위 내에서
        if 0 <= nx < R and 0 <= ny < C:
            
            # 2. 방문하지 않았고 벽이 아님
            if dist_jihoon[nx][ny] < 0 and board[nx][ny] != '#':
                
                # 3. 방문하려는 곳이 불이 번지지 않았음 또는 지훈이가 갈 경우 걸리는 시간이 이미 불이 번진 시간보다 작은 경우
                if dist_fire[nx][ny] == -1 or dist_jihoon[a][b] + 1 < dist_fire[nx][ny]:
                    dist_jihoon[nx][ny] = dist_jihoon[a][b] + 1
                    queue_jihoon.append((nx,ny))
        else:
            print(dist_jihoon[a][b] + 1)
            exit(0)

else:
    print("IMPOSSIBLE")