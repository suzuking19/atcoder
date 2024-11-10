# N = int(input())
# A_list = list(map(int, input().split()))

# ans = []

# for i in range(N):
#     match = -1
#     for j in range(i-1, -1, -1):
#         if A_list[i] == A_list[j]:
#             match = j + 1
#             break
#     ans.append(match)

# print(*ans)

N = int(input())
A = list(map(int, input().split()))
last = {}
B = [-1] * N
# Aの要素の数だけ繰り返す
for i in range(N):
    # もしlastにAのi番目の要素が格納されていたら
    if A[i] in last:
        # Bのi番目の要素に、last[Aのi番目の要素]の値を登録する
        B[i] = last[A[i]]
    # Aのi番目の要素をlastに登録する
    # この内容を参照してBを登録する
    # インデックス番号ではないので、1を加える
    last[A[i]] = i + 1

print(*B)