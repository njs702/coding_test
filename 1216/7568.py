# 덩치

n = int(input())

people = []
rank = [1] * n # 사람들의 덩치 순위 저장 리스트

for i in range(n): # 사람들 정보 입력받기
    x,y = map(int,input().split())
    people.append([x,y])
    
for i in range(n):
    for j in range(n):
        # 몸무게와 키 모두 작다면 랭크 증가
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1
        
        else:
            continue
        

for i in range(n):
    print(rank[i],end=" ")