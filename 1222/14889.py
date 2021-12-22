from itertools import combinations

minimum = 1e9
n = int(input())
board = []

for i in range(n):
    board.append(list(map(int,input().split())))
    
members = combinations(range(n), n//2)

for member in members:
    start = set(member) # set 형태로 계산하기 위해 set 자료형 변환
    link = list(set(range(n)) - start) # 0부터 n-1 까지 중에 start 팀에 없는 사람들로 구성
    start = list(start)
    
    start_sum = 0 # 스타트팀 능력치 합
    link_sum = 0 # 링크팀 능력치 합
    
    for i in range(n//2):
        for j in range(i+1,n//2):
            start_sum += board[start[i]][start[j]] + board[start[j]][start[i]] # 스타트팀 능력치 합 구하기
            link_sum += board[link[i]][link[j]] + board[link[j]][link[i]] # 링크팀 능력치 합 구하기
    
    minimum = min(minimum,abs(start_sum-link_sum))

print(minimum)


