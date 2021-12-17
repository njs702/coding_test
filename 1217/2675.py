t = int(input())
result = []

for i in range(t):
    temp_str = ""
    r,s = input().split()
    s = list(s)
    for j in range(len(s)):
        for _ in range(int(r)):
            temp_str += s[j]
    result.append(temp_str)
    
for i in result:
    print(i)