from collections import defaultdict

S = input()

if len(S) % 2 == 1:
    print("No")
    exit()

half = len(S) // 2
for i in range(half):
    idx = 2 * i
    if S[idx] != S[idx+1]:
        print("No")
        exit()

count = defaultdict(int)
for i in range(len(S)):
    count[S[i]] += 1

for i in count.values():
    if i != 2:
        print("No")
        exit()
print("Yes")