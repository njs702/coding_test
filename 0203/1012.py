import sys
sys.setrecursionlimit(10000)

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    global count
    visited[y][x] = count
    # 상,하,좌,우로 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if visited[ny][nx] == 0 and field[ny][nx] == 1:
                dfs(nx,ny)

T = int(sys.stdin.readline())

for _ in range(T):
    count = 1
    M,N,K = map(int,sys.stdin.readline().split())
    field = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    # 입력받은 값으로 field에 배추 위치 저장
    for _ in range(K):
        X,Y = map(int,sys.stdin.readline().split())
        field[Y][X] = 1

    # # 배추밭 출력 확인용
    # for i in field:
    #     print(i)

    # 좌표 순회하며 탐색
    for y in range(N):
        for x in range(M):
        # 만약 해당 좌표 방문하지 않은 상태고, 배추가 심어져 있다면 해당 위치에서 탐색 시작
            if visited[y][x] == 0 and field[y][x] == 1:
                dfs(x,y)
                count += 1
    
    # # 방문 출력 확인용
    # print("=====chnage visited array=====")
    # for i in visited:
    #     print(i)

    print(count-1)





