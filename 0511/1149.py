import sys

# i번쨰 집을 칠할 때 최소 비용 D[i]
# D[i][0] : 최소 비용인데, 집의 색을 빨간색으로 칠함
# D[i][1] : 최소 비용인데, 집의 색을 초록색으로 칠함
# D[i][2] : 최소 비용인데, 집의 색을 파란색으로 칠함

# D[k][0] = min(D[k-1][1],D[k-1][2]) + R[k]
# D[k][1] = min(D[k-1][0],D[k-1][2]) + G[k]
# D[k][2] = min(D[k-1][0],D[k-1][1]) + B[k]

# D[1][0] = R[1]
# D[1][1] = G[1]
# D[1][2] = B[1]

N = int(sys.stdin.readline())
houses = []
D = [[0]*3 for _ in range(1005)]
R = [0]*1005
G = [0]*1005
B = [0]*1005

for i in range(1,N+1):
    R[i],G[i],B[i] = map(int,sys.stdin.readline().split())

D[1][0] = R[1]
D[1][1] = G[1]
D[1][2] = B[1]

for i in range(2,N+1):
    D[i][0] = min(D[i-1][1],D[i-1][2]) + R[i]
    D[i][1] = min(D[i-1][0],D[i-1][2]) + G[i]
    D[i][2] = min(D[i-1][0],D[i-1][1]) + B[i]

print(min(D[N][0],D[N][1],D[N][2]))