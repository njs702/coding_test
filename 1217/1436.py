# 영화감독 숌

n = int(input())
result = 0
num = 0

while True:
    
    num_to_str = str(num) # 숫자를 문자열로 변환
    if '666' in num_to_str: # 666이 문자열에 포함되어 있으면 개수 증가
        result += 1
    if result == n:
        print(num)
        break
    else:
        num += 1
    
    

