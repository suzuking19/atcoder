position = [[0 for _ in range(8)] for _ in range(8)]

rows = []

for i in range(8):
    row = input()
    rows.append(row)

for i in range(8):
    row_list = list(rows[i])
    for j in range(8):
        if row_list[j] == "#":
            row_num = i
            col_num = j
            
            position[i][0] = 1
            position[i][1] = 1
            position[i][2] = 1
            position[i][3] = 1
            position[i][4] = 1
            position[i][5] = 1
            position[i][6] = 1
            position[i][7] = 1
            position[0][j] = 1
            position[1][j] = 1
            position[2][j] = 1
            position[3][j] = 1
            position[4][j] = 1
            position[5][j] = 1
            position[6][j] = 1
            position[7][j] = 1

ans = 0

for i in range(8):
    for j in range(8):
        if position[i][j] == 0:
            ans += 1

print(ans)