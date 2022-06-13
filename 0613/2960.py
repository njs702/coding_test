import sys

n,k = map(int,sys.stdin.readline().split())

numbers = [i for i in range(n+1)]
isPrime = [True] * (n+1)

temp = 0

for i in range(2,n+1):
    for j in range(i,n+1,i):
        if isPrime[j]:
            isPrime[j] = False
            temp += 1
            if temp == k:
                print(j)
                break

