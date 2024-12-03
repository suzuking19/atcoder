N, D = map(int, input().split())
S = input()

cookie_idx = []

for i in range(len(S)):
    if S[i] == "@":
        cookie_idx.append(i)

ans = []
ans = list(S)

for i in range(1, D+1):
    eaten_cookie_idx = cookie_idx[-(i)]
    ans[eaten_cookie_idx] = "."

ans = ''.join(ans)

print(ans)