# 좌표 압축

# 리스트의 경우 시간 복잡도 O(N), 딕셔너리의 경우 O(1)
n = int(input())
numbers = []

numbers = list(map(int,input().split()))
temp_set = set(numbers) # 중복된 숫자를 제거하기 위한 집합 자료형으로의 변환 
temp_list = list(temp_set) # 집합 자료형을 리스트 자료형으로 변환 [2,4,-10,-9]

temp_list.sort() # 오름차순 정렬 [-10,-9,2,4]
dic = {temp_list[i]:i for i in range(len(temp_list))} # 딕셔너리 자료형 변환 

for i in numbers:
    print(dic[i],end=" ")