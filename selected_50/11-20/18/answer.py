import itertools

s, k = map(str, input().split())
k = int(k)

s_set = set()

for p in itertools.permutations(range(len(s))):

    temp = ""

    for i in p:
        temp += s[i]

    s_set.add(temp)

s_list = list(s_set)
s_list.sort()

print(s_list[k-1])