import queue
import sys
from collections import deque

n,m,v = map(int,sys.stdin.readline().split())
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(v):
    visited_dfs[v] = True
    print(v,end=" ")
    for i in range(1,n+1):
        if visited_dfs[i] == False and graph[v][i] == 1:
            dfs(i)
    pass

def bfs(v):
    queue = deque()
    queue.append(v)
    visited_bfs[v] = True
    while queue:
        v = queue.popleft()
        print(v,end = " ")
        for i in range(1,n+1):
            if visited_bfs[i] == False and graph[v][i] == 1:
                queue.append(i)
                visited_bfs[i] = True

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    # graph 간선 연결
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)