s = input().split()
words = set(s)
d = {word: s.count(word) for word in words}
sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

for key in sorted_d.keys():
    print(key)
