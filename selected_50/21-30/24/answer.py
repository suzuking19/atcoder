# TLE
# H, W, N = map(int, input().split())

# row_list = []
# col_list = []

# for _ in range(N):
#     A, B = map(int, input().split())
#     row_list.append(A)
#     col_list.append(B)

# row_list_set = set(row_list)
# row_list_set = list(row_list_set)
# row_list_set.sort()

# col_list_set = set(col_list)
# col_list_set = list(col_list_set)
# col_list_set.sort()

# for i in range(N):
#     row = row_list_set.index(row_list[i]) + 1
#     col = col_list_set.index(col_list[i]) + 1
#     print(row, col)

# indexを使うと先頭から探すため10^9の数字なども先頭から探す必要になりTLEになってしまう

H, W, N = map(int, input().split())

cards = []
rows = []
cols = []

for _ in range(N):
    A, B = map(int, input().split())
    cards.append((A, B))
    rows.append(A)
    cols.append(B)

rows = set(rows)
rows = list(rows)
rows.sort()

rows_converter = {}

for i in range(len(rows)):
    rows_converter[rows[i]] = i + 1

cols = set(cols)
cols = list(cols)
cols.sort()

cols_converter = {}

for i in range(len(cols)):
    cols_converter[cols[i]] = i + 1

for i in range(len(cards)):
    row = rows_converter[cards[i][0]]
    col = cols_converter[cards[i][1]]
    print(row, col)
