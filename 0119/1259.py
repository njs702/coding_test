import sys

while True:
    n = input()
    front = []
    back = []
    if n == '0':
        break
    for i in range(len(n)//2):
        front.append(n[i])
    if len(n) % 2 == 0:
        for i in range(-1,-len(n)//2 - 1,-1):
            back.append(n[i])
    else:
        for i in range(-1,-len(n)//2,-1):
            back.append(n[i])
    if front == back:
        print("yes")
    else:
        print("no")