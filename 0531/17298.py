import sys

n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

_result = [-1]*n
_stack = []

for i in range(n):
    while _stack and numbers[_stack[-1]] < numbers[i]:
        
        _result[_stack.pop()] = numbers[i]
    _stack.append(i)

print(*_result)