from math import gcd

n = int(input())
for i in range(n):
    n,m = map(int,input().split())
    GCD = gcd(n,m)
    LCM = n * m // GCD
    print(LCM)