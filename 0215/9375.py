import sys

T = int(sys.stdin.readline())
for _ in range(T):
    input_clothes = []
    n = int(sys.stdin.readline())
    count = n
    for i in range(n):
        clothes = sys.stdin.readline().split()
        input_clothes.append(clothes)
        