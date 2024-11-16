N = input()

num_dict = {1:0,2:0,3:0}

for i in range(len(N)):
    if N[i] == "1":num_dict[1] += 1
    elif N[i] == "2":num_dict[2] += 1
    elif N[i] == "3":num_dict[3] += 1

if num_dict[1] == 1 and num_dict[2] == 2 and num_dict[3] == 3:
    print("Yes")
else:
    print("No")