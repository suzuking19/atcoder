n = int(input())

ans = 0
section_list = []

for _ in range(n):
    section_info = list(map(int, input().split()))
    
    if section_info[0] == 1:
        section_list.append([section_info[1], section_info[2]])
    elif section_info[0] == 2:
        section_list.append([section_info[1], section_info[2]-0.1])
    elif section_info[0] == 3:
        section_list.append([section_info[1]+0.1, section_info[2]])
    elif section_info[0] == 4:
        section_list.append([section_info[1]+0.1, section_info[2]-0.1])

for i in range(n):
    for j in range(i+1, n):
        il = section_list[i][0]
        ir = section_list[i][1]
        jl = section_list[j][0]
        jr = section_list[j][1]

        if il <= jr <= ir:
            ans += 1
        elif il <= jl <= ir:
            ans += 1
        elif jl <= il <= jr:
            ans += 1
        elif jl <= ir <= jr:
            ans += 1

print(ans)