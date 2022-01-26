import sys
import math

# A = 낮에 올라가는 거리
# B = 잠을 자면서 떨어지는 거리
# V = 나무의 높이
A,B,V = map(int,sys.stdin.readline().split())

# A * day - B * (day-1) >= V   // 마지막날에 잠을 자면서 떨어지지 않아도 됨
# (A-B) * day >= V - B
# day = (V-B) / (A-B) 

day = (V-B) / (A-B)
print(math.ceil(day))







