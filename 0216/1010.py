import sys

# mCn 구하기

def fact(num):
    result = 1
    for i in range(1,num+1):
        result *= i
        
    return result

T = int(sys.stdin.readline())
for _ in range(T):
    N,M = map(int,sys.stdin.readline().split())
    up = fact(M)
    down = fact(N) * fact(M-N)
    print(up // down)
    