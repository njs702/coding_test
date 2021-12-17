# 통계학
from collections import Counter # 최빈값 찾기 위한 라이브러리

sum = 0
average = 0 # 산술평균
mid = 0 # 중앙값
freq = 0 # 최빈값
ran = 0 # 범위

n = int(input())

numbers = []
for i in range(n):
    numbers.append(int(input()))
    
numbers.sort()

for number in numbers:
    sum += number
average = sum / n
print(f'{average :.0f}')

mid = numbers[int(n/2)]
print(mid)

c = Counter(numbers)
mode = c.most_common(n)
if len(mode) == 1: 
    freq = mode[0][0]
elif mode[0][1] == mode[1][1]:
    freq = mode[1][0]
else :
    freq = mode[0][0]
print(freq)

ran = numbers[n-1] - numbers[0]
print(ran)
    
