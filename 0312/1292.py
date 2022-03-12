import sys

A,B = map(int,sys.stdin.readline().split())
numbers = []
# A-1 번째부터 B 번째까지의 합을 구한다.

for i in range(1,B+1):
    for j in range(1,i+1):
        numbers.append(i)
sum = 0

for n in range(A-1,B):
    sum += numbers[n]

print(sum)