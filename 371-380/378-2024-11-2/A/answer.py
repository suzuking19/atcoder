A_list = list(map(int, input().split()))

ans = 0

A_dict = {1:0, 2:0, 3:0, 4:0}

for i in A_list:
    if i == 1:A_dict[1] += 1
    elif i == 2:A_dict[2] += 1
    elif i == 3:A_dict[3] += 1
    elif i == 4:A_dict[4] += 1

for i in range(1,5):
    if A_dict[i] == 2:
        ans += 1
    elif A_dict[i] == 3:
        ans += 1
    elif A_dict[i] == 4:
        ans += 2

print(ans)