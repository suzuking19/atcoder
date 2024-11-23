N = int(input())
S = input()

con_list = []
con_str_len = 0
for i in range(N):
    if i == 0:
        con_str_len += 1
    elif i == N - 1:
        if S[i] == S[i-1]:
            con_str_len += 1
            con_list.append([S[i], con_str_len])
        else:
            con_list.append([S[i-1], con_str_len])
            con_list.append([S[i], 1])
    else:
        if S[i] == S[i-1]:
            con_str_len += 1
        else:
            con_list.append([S[i-1], con_str_len])
            con_str_len = 1

ans = 1

for i in range(len(con_list)-2):
    if con_list[i+1][0] != "/" or con_list[i+1][1] != 1:
        continue
    if con_list[i][0] != "1":
        continue
    if con_list[i+2][0] != "2":
        continue
    
    comp_ans = min(con_list[i][1], con_list[i+2][1]) * 2 + 1
    ans = max(ans, comp_ans)

print(ans)