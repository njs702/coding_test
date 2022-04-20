import sys

# T = 상담을 완료하는 데 걸리는 기간
T = []
# P = 상담을 했을 때 받을 수 있는 금액
P = []

# 상담을 했을 때 나오는 모든 금액 저장 리스트
money = []

N = int(sys.stdin.readline())
# dp = 뒤에서부터 계산해 오며 수익을 비교 할 리스트
dp = [0 for _ in range(N+1)]

for i in range(N):
    t,p = map(int,sys.stdin.readline().split())
    T.append(t)
    P.append(p)

for i in range(N-1,-1,-1):
    if i + T[i] > N:
        dp[i] = dp[i+1]
    else:
        # N+1 일 기준 수익과, N번째 날의 수익 + T[i]일 이후의 수익 중 더 큰 값을 선택
        dp[i] = max(dp[i+1],P[i] + dp[i+T[i]])

print(dp[0])
        

