import sys

N,M = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))
_result = []

numbers.sort()

def dfs(start):

    if len(_result) == M:
        print(' '.join(map(str,_result)))
        return
    
    for i in range(start,N):
        _result.append(numbers[i])
        dfs(i)
        _result.pop()
        
dfs(0)