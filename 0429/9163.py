from itertools import combinations
import sys
from math import gcd

t = int(sys.stdin.readline())

for _ in range(t):
    gcd_list = []
    numbers = list(map(int,sys.stdin.readline().split()))
    n = numbers[0]
    del numbers[0]
    
    # 숫자들 GCD 합
    
    for com in combinations(numbers,2):
        # print(list(com))
        gcd_list.append(gcd(list(com)[0],list(com)[1]))
    
    print(sum(gcd_list))
