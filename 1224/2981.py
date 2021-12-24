n = int(input())
numbers = []
array = []

for i in range(n):
    numbers.append(int(input()))

for m in range(2,max(numbers)+1):
    for i in numbers:
        array.append(i%m)
    temp = set(array)
    if len(temp) == 1:
        print(m,end= " ")
    else:
        temp = set()
