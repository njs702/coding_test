import sys
from math import lcm

T = int(sys.stdin.readline())
for _ in range(T):
    M,N,x,y = map(int,sys.stdin.readline().split())
    if M == x: x = 0
    if N == y: y = 0
    # M으로 나눴을 때 나머지가 x, N으로 나눴을 떄 나머지가 y인 수
    for i in range(x,lcm(M,N)+1,M):
        if i == 0: continue
        if i % N == y:
            print(i)
            break
    else:
        print(-1)
        
    
    