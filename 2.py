N = int(input())
d = {}
for i in range(N):
    data = input().split()
    d[data[0]] = data[1]

phrase = input().split()
for word in phrase:
    if word in d:
        print(d[word], end=' ')
    else:
        print(word, end=' ')
