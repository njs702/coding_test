# 분해합

n = int(input())


for i in range(1,n+1):
    result = 0 # 결과 저장 변수 초기화
    result += i # 숫자를 더함
    temp_str = str(i) # 숫자를 문자열로 변환
    temp_list = list(temp_str) # 문자열을 리스트 형태로 변환
    temp_num = list(map(int,temp_list)) # 문자열 리스트를 정수 리스트로 변환
    
    for j in temp_num:
        result += j # 각 자리수를 더함
    
    if result == n: # 숫자를 더한 값이 입력같과 같다면 생성자
        print(i)
        break
    
    if i == n:
        print(0)
        break

    