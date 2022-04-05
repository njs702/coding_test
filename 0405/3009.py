import sys

x_num = []
y_num = []
result_x = 0
result_y = 0

for _ in range(3):
    x,y = map(int,sys.stdin.readline().split())
    x_num.append(x)
    y_num.append(y)

for i in range(3):
    if x_num.count(x_num[i]) == 1:
        result_x = x_num[i]
    if y_num.count(y_num[i]) == 1:
        result_y = y_num[i]

print(result_x,result_y)
    