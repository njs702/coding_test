import sys

n = sys.stdin.readline()


for i in range(0,len(n),10):
    print(n[i:i+10])