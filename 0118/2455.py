import sys

people = []
current = 0

for i in range(4):
    t_out,t_in = map(int,sys.stdin.readline().split())
    current = current + t_in - t_out
    people.append(current)

print(max(people))

    