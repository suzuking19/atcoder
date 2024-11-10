N, K = map(int, input().split())
S = input()

teeth = []
is_start = False

for i in range(len(S)):
    if S[i] == "X":
        is_start = False

    if S[i] == "O" and not is_start:
        is_start = True
        teeth.append(0)

    if S[i] == "O" and is_start:
        teeth[-1] += 1

ans = 0

for i in range(len(teeth)):
    is_eating = True

    while is_eating:
        if teeth[i] >= K:
            teeth[i] -= K
            ans += 1
        else:
            is_eating = False

print(ans)
