N = int(input())
d = {}
for i in range(N):
    data = input().split()
    d[data[0]] = data[1]

phrase = input()

f = 0
for key, value in d.items():
    if key == phrase:
        print(value)
        f = 1
        break
    elif value == phrase:
        print(key)
        f = 1
        break

if f == 0:
    print(phrase)
