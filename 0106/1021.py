from collections import deque
import sys

count = 0

queue = deque()

# n : 큐의 크기, m : 뽑아내려고 하는 수의 개수
n,m = map(int,sys.stdin.readline().split())

# 뽑아낼 원소들의 위치 , [2,9,5]
positions = list(map(int,sys.stdin.readline().split())) 

for i in range(1,n+1):
    queue.append(i)

while positions:
    
    if queue[0] == positions[0]:
        queue.popleft()  # 가장 앞의 숫자가 뽑아야 할 숫자면 pop
        del positions[0]
        
    else:
        # 왼쪽에 가까운지 check
        if queue.index(positions[0]) <= len(queue)/2: # 2번연산 시행
            while queue[0] != positions[0]:
                queue.append(queue.popleft())
                count += 1
                
        # 오른쪽에 가까운지 check        
        else:
            while queue[0] != positions[0]: # 3번연산 시행
                queue.appendleft(queue.pop())
                count += 1
   

print(count)
