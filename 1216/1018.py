# 체스판 다시 칠하기
# 매트릭스의 인덱스 규칙을 활용해 푸는 문제

# 행과 열의 합이 짝수일 경우, 행과 열의 합이 홀수일 경우로 나누어 계산

def printboard():
    for i in board:
        for j in i:
            print(j,end="")
        print()

n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
count = []

for i in range(n-7):
    for j in range(m-7):  # n과m의 입력값이 8보다 크다. 8x8 배열로 반복하는 횟수
        first_w = 0 # 첫 시작이 w인 경우 변경해야 할 체스판의 수
        first_b = 0 # 첫 시작이 b인 경우 변경해야 할 체스판의 수
        
        for a in range(i,i+8):
            for b in range(j,j+8): # 8x8로 잘라진 범위 내에서 탐색
                if (a+b) % 2 == 0: # 행과 열의 합이 짝수인 경우 -> 첫 번째 체스판의 색깔과 같아야 한다
                    if board[a][b] != 'W': 
                        first_w += 1  # 첫 번째 체스판이 W인 경우, 만약 현재 탐색중인 체스판이 W가 아니라면 W로 바꿔줘야 하므로 first_w 값 증가
                    if board[a][b] != 'B':
                        first_b += 1 # 첫 번째 체스판이 B인 경우, 동일하게 진행
                else: # 행과 열의 합이 홀수인 경우 -> 첫 번째 체스판의 색깔과 달라야 한다
                    if board[a][b] != 'B':
                        first_w += 1
                    if board[a][b] != 'W':
                        first_b += 1
                    
        count.append(min(first_w,first_b))

print(min(count))




