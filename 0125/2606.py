import sys

# 노드 개수
n = int(sys.stdin.readline())
# 간선 개수
m = int(sys.stdin.readline())

count = 0

visited = [False] * (n+1) # n+1인 이유는 노드의 번호가 인덱스로 오기 때문
c_graph = [[0]*(n+1) for _ in range(n+1)] # 마찬가지로 n+1개의 그래프 노드

def dfs(v):
    # 먼저 방문 노드 방문처리
    visited[v] = True
    
    # 노드들을 순차적으로 탐색(1번부터 n+1번째 노드까지)
    for i in range(n+1):
        # 만약 다음 탐색하는 노드가 방문하지 않았고, 지금 탐색중인 노드와 연결되어 있다면 
        if visited[i] == False and c_graph[v][i] == 1:
            # 해당 노드에서 다시 dfs탐색 시작
            dfs(i)

# 노드들 그래프로 만든다 (간선 연결)
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    c_graph[a][b] = c_graph[b][a] = 1

# 1번 노드부터 전염 시작
dfs(1)

for i in range(n+1):
    if visited[i] == True:
        count += 1

# 1번 노드는 무조건 바이러스 감염 PC, 1개를 빼 주어야 한다.
print(count-1)
