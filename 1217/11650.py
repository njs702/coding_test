# 좌표 정렬하기

n = int(input())
array = []
for i in range(n):
    x,y = map(int,input().split())
    array.append((x,y))

array.sort()
for i in array:
    print(i[0],end=" ")
    print(i[1])