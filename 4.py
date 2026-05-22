N = int(input())
d = {}

for i in range(N):
    data = input().split()
    d[data[0]] = data[1:]

phrase = input()
for key, value in d.items():
    if phrase in value:
        print(key)
        break
