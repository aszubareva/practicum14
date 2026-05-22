def descendant_count(parent: str, fam: dict) -> int:
    if parent not in fam:
        return 0

    count = 0
    for child in fam[parent]:
        count += (1 + descendant_count(child, fam))
    return count


N = int(input())
family = {}
for i in range(N):
    data = input().split()
    if data[0] not in family:
        family[data[0]] = [data[1]]
    else:
        family[data[0]].append(data[1])


person = input()
print(descendant_count(person, family))
