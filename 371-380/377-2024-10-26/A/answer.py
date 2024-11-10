S = input()

collect = {"A": 0, "B": 0, "C": 0}

S_list = list(S)

for i in S_list:
    if i == "A":collect["A"] += 1
    elif i == "B":collect["B"] += 1
    elif i == "C":collect["C"] += 1

judge = 0

for i in collect:
    if collect[i] == 1:
        judge += 1

if judge == 3:
    print("Yes")
else:
    print("No")

