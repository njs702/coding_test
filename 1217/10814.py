# 나이순 정렬

n = int(input())
people = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    people.append((age, name))
    
# 우선순위 정렬
# 1. 나이가 증가하는 순서
# 2. 나이가 같으면 먼저 가입한 사람이 오는 순서

people.sort(key = lambda x : x[0]) # 나이가 증가하는 순서대로 정렬

for i in people:
    print(i[0],i[1])