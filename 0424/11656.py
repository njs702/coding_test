import sys

a_list = []
a = sys.stdin.readline().rstrip()

for i in range(len(a)):
    a_list.append(a[i:])
a_list.sort()

for i in a_list:
    print(i)