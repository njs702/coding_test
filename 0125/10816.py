import sys
result = []

# 딕셔너리 활용해서 문제 풀어보기

n = int(sys.stdin.readline())
n_numbers = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_numbers = list(map(int,sys.stdin.readline().split()))

n_dict = dict()

for n in n_numbers:
    if n in n_dict:
        n_dict[n] += 1
    else:
        n_dict[n] = 1

for m in m_numbers:
    if m in n_dict:
        print(n_dict[m],end=" ")
    else:
        print(0,end=" ")