import sys

T = int(sys.stdin.readline())

for _ in range(T):
    order = input()
    N = int(sys.stdin.readline())
    num_str = list(sys.stdin.readline().rstrip()[1:-1].split(","))
    #num_str[0],num_str[-1] = '\0','\0'
    print(num_str)

print() 