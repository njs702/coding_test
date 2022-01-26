import sys

T = int(sys.stdin.readline())
for _ in range(T):
    H,W,N = map(int,sys.stdin.readline().split())
    # 만약 나누어 떨어지면  
    if N % H == 0:
        first = H # 맨 위 층이 된다.
        second = N // H
    else:
        first = N % H
        second = N // H + 1
    
    if second < 10:
        print(str(first)+"0"+str(second))
    else:
        print(str(first)+str(second))
