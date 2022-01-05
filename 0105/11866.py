from collections import deque
import sys

queue = deque()
n,k = map(int,sys.stdin.readline().split())

for i in range(1,n+1):
    queue.append(i) # 1부터 N까지의 숫자 queue에 넣기


