import sys

_set = 0
n = sys.stdin.readline()
length = len(n) - 1
_arr = [0,0,0,0,0,0,0,0,0,0]


for i in range(length):
    # 9와 6을 바꿀 수 있으므로 9가 나온경우 6의 개수에 저장
    if n[i] == '6':
        _arr[9] += 1
    else:
        _arr[int(n[i])] += 1

if _arr[9] % 2 == 0:
    temp = _arr[9] // 2
else:
    temp = _arr[9] // 2 + 1

_max = max(max(_arr[0:9]),temp)
print(_max)
        

