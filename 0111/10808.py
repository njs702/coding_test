import sys

n = input()
words = [0]*26

for word in n:
    words[ord(word)-97] += 1

print(*words)