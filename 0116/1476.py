import sys

first_E,first_S,first_M,count = 1,1,1,1

E,S,M = map(int,sys.stdin.readline().split())

while True:
    if first_E == E and first_M == M and first_S == S:
        break
    first_M += 1
    first_E += 1
    first_S += 1
    count += 1
    if first_E >=16 : first_E -=15
    if first_S >=29 : first_S -=28
    if first_M >=20 : first_M -=19
    
print(count)

