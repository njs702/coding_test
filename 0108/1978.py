# 소수 찾기
import sys

n = int(sys.stdin.readline())
numbers = []
prime_count = 0
count = 0

numbers = list(map(int,sys.stdin.readline().split()))
4

for number in numbers:
    for i in range(1,number+1):
        if number % i == 0:
            count += 1
    if count == 2:
        prime_count += 1
    count = 0

print(prime_count)
