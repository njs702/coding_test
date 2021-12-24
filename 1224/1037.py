n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
minimum = numbers[0]
maximum = numbers[n-1]
print(minimum * maximum)