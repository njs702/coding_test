# 단어 정렬

n = int(input())
words = []
for i in range(n):
    words.append(input())
words_set = set(words) # 리스트가 아닌 집합(중복 제거)
new_words = list(words_set) # 집합을 새로운 리스트로 생성

# 새로운 리스트 정렬
# 우선순위 1. 길이가 짧은 것부터
# 우선순위 2. 길이가 같으면 사전 순으로
new_words.sort()
new_words.sort(key=len)  # 우선순위가 높은 것이 가장 나중에 실행되어야 함

for i in new_words:
    print(i)