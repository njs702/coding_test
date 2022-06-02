import sys

n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

_result = [-1]*n
_stack = []

# 스택에 들어가는 것은 숫자값이 아니라 인덱스 값!!!

for i in range(n):
    while _stack and numbers[_stack[-1]] < numbers[i]:
        
        # 위의 조건을 만족한다면 해당 인덱스의 오큰수는 현재 탐색중인 인덱스에 해당하는 숫자
        _result[_stack.pop()] = numbers[i]
    _stack.append(i)

print(*_result)