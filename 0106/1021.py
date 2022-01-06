from collections import deque
import sys

count = 0

queue = deque()
# n : 큐의 크기, m : 뽑아내려고 하는 수의 개수
n,m = map(int,sys.stdin.readline().split())
position = list(map(int,sys.stdin.readline().split())) # 뽑아낼 원소들의 위치

queue.append(i for i in range(1,n+1))
print(*queue)