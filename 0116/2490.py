import sys

for i in range(3):
    temp = list(map(int,sys.stdin.readline().split()))
    if temp.count(1) == 0:
        print("D")
    if temp.count(1) == 1:
        print("C")
    if temp.count(1) == 2:
        print("B")
    if temp.count(1) == 3:
        print("A")
    if temp.count(1) == 4:
        print("E")