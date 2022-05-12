import sys

N = int(sys.stdin.readline())
D = [0]*1005
# 1. 테이블 정의하기
# D[i] = 2 x i 크기의 직사각형을 채우는 방법의 수

# 2. 점화식 찾기
# D[1] = 1
# D[2] = 2
# D[3] = 3
# D[4] = 5
# D[k] = D[k-2] + D[k-1] ?
D[1] = 1
D[2] = 2

for i in range(3,N+1):
    D[i] = D[i-1] + D[i-2]

print(D[N]%10007)