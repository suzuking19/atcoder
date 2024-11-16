N, K = map(int, input().split())
S = input()

one_start_end = []

is_one = False
start = 0
end = 0

for i in range(N):
    if S[N-1] == "0":
        if S[i] == "1" and not is_one:
            start = i
            is_one = True
        elif S[i] == "0" and is_one:
            end = i - 1
            is_one = False
            one_start_end.append([start, end])
    else:
        if S[i] == "1" and not is_one:
            start = i
            is_one = True
            # 末尾で長さ1の場合
            if i == N - 1:
                end = i
                one_start_end.append([start, end])
        elif S[i] == "0" and is_one:
            end = i - 1
            is_one = False
            one_start_end.append([start, end])
        # 末尾が長さ1以上で1で終わる場合にも対応する
        elif S[i] == "1" and is_one and i == N-1:
            end = i
            one_start_end.append([start, end])

K -= 1
K_dec_start_end = one_start_end[K-1]
K_start_end = one_start_end[K]


S_extract = S[K_dec_start_end[1]+1:K_start_end[0]]
# もしKで終わる場合も想定
if K_start_end[1] == N-1:
    S_tail = ""
else:
    S_tail = S[K_start_end[1]+1:]

ans = S[:K_dec_start_end[1]+1] + S[K_start_end[0]:K_start_end[1]+1] + S_extract + S_tail
print(ans)