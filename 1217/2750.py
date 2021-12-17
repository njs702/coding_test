# 수 정렬하기

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

numbers.sort()

for i in range(n):
    print(numbers[i])