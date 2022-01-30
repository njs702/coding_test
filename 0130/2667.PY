import queue
import sys
from collections import deque

# bfs는 queue에 넣고 빼면서 탐색
count = 1
num_of_apart = 0
result = []

# 방향 확인용 좌표
dx = [-1,1,0,0]
dy = [0,0,1,-1]

# bfs 탐색 구현
def bfs(x,y):
    global num_of_apart
    apart_queue = deque()
    apart_queue.append((x,y))
    
    # 해당 좌표 방문 처리
    visited[x][y] = count

    if apart[x][y] == 1:
        num_of_apart += 1

    while apart_queue:
        a,b = apart_queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if apart[nx][ny] == 1 and visited[nx][ny] == 0:
                    bfs(nx,ny)

N = int(sys.stdin.readline())

# 해당 좌표 방문 체크 그래프
visited = [[0]*N for _ in range(N)] 
apart = []

# 아파트 위치 초기화 , 연결되어 있는 문자열 분리하는 법 잊지 말기
for x in range(N):
    apart.append(list(map(int,input())))

for x in range(N):
    for y in range(N):
        if apart[x][y] == 1 and visited[x][y] == 0:
            bfs(x,y)
            result.append(num_of_apart)
            num_of_apart = 0
            count += 1
result.sort()

print(count-1)
for i in result:
    print(i)

# for i in apart:
#     print(i)

# for i in visited:
#     print(i)
        
