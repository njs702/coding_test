import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())
visited = [0 for _ in range(100001)]
dist_queue = deque()
dist_queue.append(N)
# 걷는다면 X-1 또는 X+1
# 순간이동은 2*X로 이동

# 1초에 갈 수 있는 곳 : 4,6,10
# 2초에 갈 수 있는 곳 : 3,5,7,8,9,11,12,20
# 3초에 갈 수 있는 곳 : .... 매우 많음
# 4초에 갈 수 있는 곳 : .... 매우 많음

# for i in (a,b,c):
#   print(i) // a,b,c 출력

while dist_queue:
    x = dist_queue.popleft()
    if x == K:
        print(visited[x])
        break
    
    for i in (x-1,x+1,2*x):
        if 0 <= i <= 100000:
            if not visited[i]:
                visited[i] = visited[x] + 1
                dist_queue.append(i)

