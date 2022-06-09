import sys

N,M = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))
_result = []
numbers.sort()


visited = [False for _ in range(N)]

def dfs(start):
    if len(_result) == M:
        print(' '.join(map(str,_result)))
        return
    
    pre = 0
    for i in range(start,N):
        
        # 같은 숫자 한번 더 쓰는 거 방지
        # if visited[i] : continue
        
        # 배열 안에 같은 숫자가 있을 경우, 중복 출력 방지
        if pre == numbers[i] : continue
        
        _result.append(numbers[i])
        visited[i] = True
        pre = numbers[i]
        dfs(i)
        _result.pop()
        visited[i] = False

dfs(0)