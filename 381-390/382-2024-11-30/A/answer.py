N, D = map(int, input().split())
S = input()

cookie = 0

for i in range(len(S)):
    if S[i] == "@":
        cookie += 1

empty = N - cookie
empty += D

print(empty)
