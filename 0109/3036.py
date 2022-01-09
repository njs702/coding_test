import sys
from math import gcd

def lcm(x,y):
    return x * y // gcd(x,y)

n = int(sys.stdin.readline())
numbers = []
numbers = list(map(int,sys.stdin.readline().split()))

for i in range(1,n):
    GCD = gcd(numbers[0],numbers[i])
    first = numbers[0] // GCD
    second = numbers[i] // GCD
    print(first,end='/')
    print(second)