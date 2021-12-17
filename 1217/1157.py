n = input().lower()

freq = [0] * 26 # 빈도수를 저장하기 위한 리스트

for i in n:
    freq[int(ord(i))-97] += 1 # 복잡하지만, 입력받은 문자열에서 해당 문자의 개수를 증가시키고 freq 리스트에 저장
    
max = max(freq) # 빈도 수 리스트에서 가장 큰 값

if freq.count(max) > 1: # 만약 max값이 여러번 등장한다면 ? 출력
    print("?")
else:
    print(chr(freq.index(max) + 97).upper()) # 아닐 경우 해당하는 max값 대문자로 출력

