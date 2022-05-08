import sys

T = int(sys.stdin.readline())

# D[4] = 7
# 맨 뒤가 1로 끝남
# 1 + 1 + 1 + 1, 1 + 2 + 1, 2 + 1 + 1, 3 + 1
# 맨 뒤가 2로 끝남
# 1 + 1 + 2, 2 + 2,
# 맨 뒤가 3으로 끝남
# 1 + 3

# 맨 뒤를 제외하고 보면, 결국 D[3]을 1,2,3으로 만드는 방법 개수 +
# D[2]을 1,2,3으로 만드는 방법 개수 +
# D[1]을 1,2,3으로 만드는 방법 개수 = 4 + 2 + 1 = 7

# D[K] = D[K-1] + D[K-2] + D[K-3]


for _ in range(T):
    D = [0] * 12
    D[1],D[2],D[3] = 1,2,4
    n = int(sys.stdin.readline())
    
    for i in range(4,n+1):
        D[i] = D[i-1] + D[i-2] + D[i-3]
    
    print(D[n])
    