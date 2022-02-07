import imp
import sys

# 해당 단지의 아파트 개수를 세기 위한 변수
apart_nums = 0

result = []
cnt = 1

#  좌/우/위/아래 방향 확인용 좌표
dx = [-1,1,0,0]
dy = [0,0,1,-1]

n = int(sys.stdin.readline())
apart = [list(map(int,input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def dfs(x,y):
    global apart_nums
    # 방문한 좌표 방문처리
    visited[x][y] = cnt
    if apart[x][y] == 1:
        apart_nums += 1
    
    # 해당 x,y 좌표에서 상,하,좌,우 방향으로 탐색 시작
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 구간을 벗어나지 않는다면
        if 0 <= nx < n and 0 <= ny < n:
            # 상,하,좌,우로 탐색하면서 해당 노드가 연결되어있는 아파트고 방문하지 않은 상태라면
            if apart[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx,ny)

# 좌표마다 dfs 탐색 시행
for x in range(n):
    for y in range(n):
        # 만약 아파트이고, 방문하지 않은 상태라면 탐색 시작
        if apart[x][y] == 1 and visited[x][y] == 0:
            dfs(x,y)
            result.append(apart_nums)
            apart_nums = 0
            cnt += 1

# # visited matrix 출력 확인용
# for a in visited:
#     print(a)

result.sort()
print(len(result))
for a in result:
    print(a)