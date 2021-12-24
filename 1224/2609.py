# 최대공약수와 최소공배수
from math import gcd

n,m = map(int,input().split())
GCD = gcd(n,m)
LCM = n * m // GCD
print(GCD)
print(LCM)