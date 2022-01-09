import sys

n,k = map(int,sys.stdin.readline().split())

up = 1
for i in range(n,n-k,-1):
    up *= i

down = 1
for i in range(1,k+1):
    down *= i

print(up//down)