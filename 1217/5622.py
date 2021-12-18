# dic = {"A":2,"B":2,"C":2,"D":3,"E":3,"F":3,"G":4,"H":4,"I":4,"J":5,"K":5,"L":5,
#        "M":6,"N":6,"O":6,"P":7,"Q":7,"R":7,"S":7,"T":8,"U":8,"V":8,"X":9,"W":9,"Y":9,"Z":9,}
# sum = 0
# n = input()
# words = list(n)

# for i in range(len(words)):
#     sum += dic[words[i]]
#     sum += 1

# print(sum)

alphabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
words = input()
sum = 0

for i in alphabet_list: # 문자열 리스트 순차 탐색
    for j in words: # 입력받은 문자열 순차 탐색
        if j in i: # 입력받은 문자열을 한 문자씩 탐색하다가, 만약 그 문자열이 i번째 리스트에 존재한다면
            sum += alphabet_list.index(i) + 3 # 해당하는 인덱스의 값 + 1 에다가 2초 더 움직여야 하므로 + 2 해준다

print(sum)