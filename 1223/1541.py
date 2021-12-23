# 최소가 되는 수 만들기
# 빼는 숫자가 크면 되기 때문에 -를 기준으로 괄호 치기

# ex) 50 - 50 + 40 - 30 + 20
expressions = list(input().split('-')) # -를 기준으로 입력받기 ["50","50+40","30+20"]
new_exp = [] # +를 기준으로 자른 리스트 생셩 [[50],[50,40],[30,20]]
new_result = [] # 해당 리스트들의 sum을 저장하는 리스트 [[50],[90],[50]]

# +를 기준으로 자른 뒤, 리스트 형태로 new_exp에 저장
for i in expressions: 
    temp = list(i.split("+"))
    new_exp.append(temp)

# new_exp에 저장되어 있는 리스트들에서 합을 구해 new_result로 저장
for i in new_exp:
    count = 0
    for j in i:
        count += int(j)
    new_result.append(count)

# 첫 번째 값은 리스트의 첫 번째 값
result = new_result[0] 

# 두 번째 값부터는 -해야 최소가 된다
for i in range(1,len(new_result)):
    result = result - new_result[i]
        
# print(new_exp)
# print(new_result)
print(result)
        
    

