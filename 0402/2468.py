import sys
from collections import deque
sys.setrecursionlimit(100000)

board = []
count_result = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]

N = int(sys.stdin.readline())
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
    
board_min = min(map(min,board)) # min in 2 dir board
board_max = max(map(max,board)) # max in 2 dir board    



# # 높이가 4 이하인 곳은 0으로 처리해줘서 물에 잠긴다
# for i in range(N):
#     for j in range(N):
#         if board[i][j] <= 4:
#             board[i][j] = 0
           
def bfs(x,y,h):
    visited[x][y] = 1
    queue = deque()
    queue.append((x,y))
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if board[nx][ny] > h:
                    bfs(nx,ny,h)
                    
for h in range(0,board_max+1):
    count = 0
    visited = [[0]*N for _ in range(N)]
    
    for x in range(N):
        for y in range(N):
            if board[x][y] > h and visited[x][y] == 0:
                bfs(x,y,h)
                count += 1
    count_result.append(count)


# for a in board:
#     print(a)

# for a in visited:
#     print(a)

print(max(count_result))