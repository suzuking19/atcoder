n = int(input())

used_judge = []
for _ in range(2*n+2):
    used_judge.append(False)

used_judge[1] = True
print(1)

while not all(used_judge):
    x = int(input())
    used_judge[x] = True

    if x == 0:
        exit()
    
    for i in range(2, len(used_judge)+1):
        if used_judge[i] == False:
            print(i)
            used_judge[i] = True
            break