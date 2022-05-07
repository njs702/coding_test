import sys


# D[i][j] - i번 째 계단을 밟았을 때, j는 연속해서 밟은 계단의 개수
# 따라서 j는 1 또는 2(연속해서 3개의 계단을 밟을 수는 없다)

# D[k][1]과 D[k][2] 구하기

# 현재까지 1개의 계단을 밟았다 -> k-1 번째 계단을 밟지 않았다
# 1. D[k][1] = max(D[k-2][1],D[k-2][2]) + S[k]
# 현재까지 2개의 계단을 밟았다 -> K-1 번째 계단을 밟았다, j=1 이어야 한다
# 2면은 3번 연속 계단을 밟은 것이 되기 때문이다
# 2. D[k][2] = D[k-1][1] + S[k]

N = int(sys.stdin.readline())
stair = [0] * 350

D = [[0]*3 for _ in range(351)]

for i in range(1,N+1):
    stair[i] = int(sys.stdin.readline())

if N == 1:
    print(stair[1])
    exit(0)

D[1][1] = stair[1]
D[1][2] = 0
D[2][1] = stair[2]
D[2][2] = stair[1] + stair[2]

for k in range(3,N+1):
    D[k][1] = max(D[k-2][1],D[k-2][2]) + stair[k]
    D[k][2] = D[k-1][1] + stair[k]

print(max(D[N][1],D[N][2]))


