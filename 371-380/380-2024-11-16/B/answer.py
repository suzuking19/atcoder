S = input()
ans = []
A_el = 0
for i in range(len(S)):
    if S[i] == "|":
        ans.append(A_el)
        A_el = 0
    elif S[i] == "-":
        A_el += 1

ans = ans[1:]
print(*ans)