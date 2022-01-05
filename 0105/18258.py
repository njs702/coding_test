from collections import deque

import sys
n = int(sys.stdin.readline())

deq = deque()

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        deq.append(int(order[1]))
    if order[0] == 'pop':
        if len(deq) <= 0:
            print(-1)
        else:
            print(deq[0])
            deq.popleft()
    if order[0] == 'size':
        print(len(deq))
    if order[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    if order[0] == 'front':
        if len(deq) <= 0:
            print(-1)
        else:
            print(deq[0])
            
    if order[0] == 'back':
        if len(deq) <= 0:
            print(-1)
        else:
            print(deq[len(deq)-1])