import math
import sys

T = int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().split())
    d = ((x1-x2)**2 + (y1-y2)**2) 
    
    # 동심원인 경우
    if d == 0 and r1 == r2:
        print(-1)
        continue
    if d == 0 and r1 != r2:
        print(0)
        continue
    
    # 두 점에서 만나는 경우
    if (r1 - r2)**2 < d < (r1 + r2)**2:
        print(2)
        continue
    # 한 점에서 만나는 경우
    if d == (r1 + r2)**2 or d == (r1 - r2)**2:
        print(1)
        continue
    # 만나지 않는 경우
    if d > (r1 + r2)**2 or d < (r1 - r2)**2:
        print(0)
        continue