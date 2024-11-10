s = input()

t_list = ["dream", "dreamer", "erase", "eraser"]

while s:
    for t in t_list:
        if s.endswith(t):
            s = s[:-len(t)]
            break
    else: 
        print("NO")
        exit()

print("YES")