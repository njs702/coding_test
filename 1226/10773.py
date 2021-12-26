import sys

n = int(sys.stdin.readline())
numbers = []

for i in range(n):
    number = int(sys.stdin.readline())
    if number == 0:
        numbers.pop()
    else:
        numbers.append(number)

sum = 0
for number in numbers:
    sum += number

print(sum)