import sys

stick = [64]
min_stick = 10000
count = 0
X = int(sys.stdin.readline())

while sum(stick) > X:    
    # 3. 남아 있는 모든 막대를 붙여서 X를 만든다
    if sum(stick) == X:
        break
    
    # 1. 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다
    min_stick = min(stick)
    stick.pop(stick.index(min_stick))
    min_stick //= 2
    
    for _ in range(2):
        stick.append(min_stick)
        
    # 2. 만약 위에서 자른 막대의 절반 중 하나를 버리고 남아있는 막대의 길이의
    # 합이 X보다 크거나 같다면, 위에서 자른 막대의 절반 중 하나를 버린다
    if sum(stick) - min_stick >= X:
        stick.pop(stick.index(min_stick))   
    
    
print(len(stick))