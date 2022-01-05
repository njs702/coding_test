from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque() # 큐 생성

for i in range(1,n+1):
    queue.append(i)

### queue에서 가장 앞에 있으면 가장 위에 있는 것 ###


# 1. 제일 위에 있는 card 바닥에 버리기 ==> 큐에서 가장 앞에것 pop
# 2. 그 다음 카드를 제일 아래 카드 밑으로 옮긴다 ==> 큐클 rotate
# ex) [2,3,4,5,6] ==> [3,4,5,6,2] 가 되는것.
# 3. 카드가 하나 남을 때 까지 앞의 과정을 반복한다

while len(queue) > 1:  # 카드가 하나 남을 때 까지 앞의 과정을 반복한다
    queue.popleft() # 제일 위에 있는 card 바닥에 버리기 ==> 큐에서 가장 앞에것 pop
    queue.rotate(-1) # 그 다음 카드를 제일 아래 카드 밑으로 옮긴다 ==> 큐클 rotate

print(queue[0])