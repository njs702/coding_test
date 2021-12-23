n = int(input())
p = []
result = 0
# p = [3,1,4,3,2] 일때, 1번 사람은 3분, 2번 사람은 1분, 3번 사람은 4분, 4번 사람은 3분, 5번 사람은 2분이 필요하다
# 최소값으로 정렬하는 것이 무조건 최소의 시간을 보장하는가?
# [1,2,3,3,4]로 정렬 후, 진행해야 하는지

p = list(map(int,input().split()))
p.sort()

for i in range(n): # 0 1 2 3 4
    for j in range(i+1): # 범위 1, 범위 2, 범위 3, 범위 4, 범위 5
        result += p[j]

print(result)
