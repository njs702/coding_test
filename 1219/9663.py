# N-Queens

# 인접한 곳에 이미 놓여져 있는 Queen이 존재하는 경우
def adjacent(x):
    for i in range(x): # i가 행, row[x] 값이 열
        if queens[x] == queens[i] or abs(queens[x] - queens[i]) == x - i:
            return False
    return True

def nqueens(x):
    global result
    if x == n: # 마지막까지 탐색을 했을 경우
        result += 1
    else:
        for i in range(n): # i가 n개의 열을 순차적으로 탐색
            queens[x] = i # 현재 깊이(depth번째 행)에 퀸이 어디에 위치하는지 추가
            if adjacent(x): # 만약 놓은 위치에서 주변에 퀸이 없다면(이 자리가 유망하다면)
                nqueens(x+1) # 다음 깊이 탐색 가능(다음 행 탐색 가능)
                
n = int(input())
result = 0
queens = [0] * n
nqueens(0)
print(result)
