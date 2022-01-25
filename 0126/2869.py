import sys
import math

# A = 낮에 올라가는 거리
# B = 잠을 자면서 떨어지는 거리
# V = 나무의 높이
A,B,V = map(int,sys.stdin.readline().split())

day = (V-B) / (A-B)
print(math.ceil(day))







