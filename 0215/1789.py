import sys

S = int(sys.stdin.readline())
count = 1

while True:
    count += 1
    if count * (count + 1) / 2 > S:
        break

print(count - 1)

