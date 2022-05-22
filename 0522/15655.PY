import sys

N,M = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))
_result = []

numbers.sort()

def dfs(start):
    
    # 길이 M만큼 되면 스택에 있는 숫자들 출력하고 맨 위에꺼 꺼내기
    if len(_result) == M:
        print(' '.join(map(str,_result)))
        return

    # 오름차순 정렬
    for i in range(start,len(numbers)):
        if numbers[i] in _result:
            continue
        
        _result.append(numbers[i])
        dfs(i+1)
        _result.pop()

dfs(0)