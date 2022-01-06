from collections import deque
import sys

queue = deque()
result = deque()
n,k = map(int,sys.stdin.readline().split())

for i in range(1,n+1):
    queue.append(i) # 1부터 N까지의 숫자 queue에 넣기

# queue에 내용이 사라질 때 까지 반복
while queue:
    # k번째 숫자를 제거해야 한다
    # ex) 3인 경우, 1과 2를 앞에서 빼고 큐의 뒤로 넣는다
    # ==> k인 경우, k-1까지의 숫자를 앞에서 빼고 큐의 뒤로 넣는다
    for i in range(k-1):
        queue.append(queue.popleft()) # queue에서 앞의 숫자들이 빠지고 뒤로 들어감
    result.append(queue.popleft()) # k번째 숫자를 뽑아서 완전히 제거

print("<",end="")
print(*result,sep=", ",end="")
print(">")
