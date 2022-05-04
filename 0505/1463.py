import sys
from collections import deque
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.

# dp 문제 풀이 순석
# 1. 테이블 정의
# 2. 점화식 찾기

# k = 12라 가정해보자
# numbers[12] = ?
# numbers[12] = numbers[11] + 1
# numbers[12] = numbers[6] + 1
# numbers[12] = numbers[4] + 1

# number[k] = min(numbers[k-1]+1,numbers[k/2]+1,numbers[k/3]+1)

# 3. 초기값 설정
numbers = [0] * 1000005

N = int(sys.stdin.readline())

numbers[1] = 0
for i in range(2,N+1):
    numbers[i] = numbers[i-1] + 1
    if i % 2 == 0 : numbers[i] = min(numbers[i],numbers[i//2] + 1)
    if i % 3 == 0 : numbers[i] = min(numbers[i],numbers[i//3] + 1)

print(numbers[N])
