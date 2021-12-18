n = int(input())
words = []

for i in range(n):
    words.append(input())

for word in words:
    for i in range(len(word)-1):
        if word[i] != word[i+1]: # 만약 현재 보는 문자와 다음 문자가 다르고 // 만약 현재 보는 문자와 같으면 다음 문자 탐색
            if word[i] in word[i+1:]: # 현재 문자가 다음 단어부터 시작하는 문자열에 포함된다면
                n -= 1 # 개수 감소
                break # 다음 단어 탐색
        

print(n)