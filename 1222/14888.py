# 연산자 끼워넣기 , 브루트포스(완전탐색) dfs
maximum = -1e9
minimum = 1e9

numbers = []

# 인덱스 순서대로 덧셈, 뺄셈, 곱셈, 나눗셈
oper = []

n = int(input())
numbers = list(map(int,input().split()))
oper = list(map(int,input().split()))

def dfs(depth, sum, plus, minus, multi, div):
    global maximum,minimum
    if depth == n: # 최대 깊이까지 탐색 마쳤을 때
        maximum = max(maximum,sum)
        minimum = min(minimum,sum)
        return
    
    if plus:
        dfs(depth + 1, sum + numbers[depth], plus - 1, minus, multi, div)
    if minus:
        dfs(depth + 1, sum - numbers[depth], plus , minus - 1, multi, div)
    if multi:
        dfs(depth + 1, sum * numbers[depth], plus , minus, multi - 1, div)
    if div:
        dfs(depth + 1, int(sum / numbers[depth]), plus , minus, multi, div - 1)
        
dfs(1,numbers[0],oper[0],oper[1],oper[2],oper[3])
print(maximum)
print(minimum)