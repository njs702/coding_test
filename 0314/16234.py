import sys

N,L,R = map(int,sys.stdin.readline().split())

# 20 <= 차이 <= 50 이면 국경선 열림

board = []

for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
