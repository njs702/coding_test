import sys

X = int(sys.stdin.readline())
line = 0
sum = 0
end = 0
number_list = []
# 1   2  6  7 15 16
# 3   5  8 14 17
# 4   9 13 18
# 10 12 19
# 11 20
# 21

# 1개, 2개, 3개, 4개, 5개, ...

while True:
    sum += line
    if sum >= X:
        break
    line += 1 # line은 몇 번쨰 대각선에 존재하는지
    end += line # end는 해당 라인의 가장 큰 수

gap = end - X # gap을 왜 구한것인가? 해당 라인에서 몇 번째 수인지 알아내기 위해?

if line % 2 == 0: # 짝수 라인이면 위에서 아래로 분모는 감소, 분자는 증가
    top = line - gap 
    bottom = gap + 1
else: # 홀수 라인이면 아래에서 위로 분모는 증가, 분자는 감소
    top = gap + 1
    bottom = line - gap    


print(str(top)+'/'+str(bottom))
  




