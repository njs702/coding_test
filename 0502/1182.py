import sys
from itertools import combinations, permutations

N,S = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))
count = 0
# numbers.sort()

# 1개부터 N개까지 부분수열 체크하기
for i in range(1,N+1):
    # i의 값에 따른 combination(중복제거) 결과
    # (-7,)
    # (-3,)
    # (-2,)
    # (5,)
    # (8,)
    # (-7, -3)
    # (-7, -2)
    # (-7, 5)
    # (-7, 8)
    # (-3, -2)
    # (-3, 5)
    # (-3, 8)
    # (-2, 5)
    # (-2, 8)
    # (5, 8)
    # (-7, -3, -2)
    # (-7, -3, 5)
    # (-7, -3, 8)
    # (-7, -2, 5)
    # (-7, -2, 8)
    # (-7, 5, 8)
    # (-3, 5, 8)
    # (-2, 5, 8)
    # (-7, -3, -2, 5)
    # (-7, -3, -2, 8)
    # (-7, -3, 5, 8)
    # (-7, -2, 5, 8)
    # (-3, -2, 5, 8)
    # (-7, -3, -2, 5, 8)
    
    for j in combinations(numbers,i):
        if sum(j) == S:
            count += 1

print(count)