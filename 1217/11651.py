# 좌표 정렬하기2

n = int(input())
array = []
for i in range(n):
    x,y = map(int,input().split())
    x,y = y,x
    array.append((x,y))
    
array.sort()

for i in array:
    print(i[1],end=" ")
    print(i[0])
