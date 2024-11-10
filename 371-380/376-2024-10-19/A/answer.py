n, c = map(int, input().split())
t_list = list(map(int, input().split()))

time = 0
get_time = 0
candy_total = 0

for i in range(n):
    time = t_list[i]
    if i == 0:
        candy_total += 1
        get_time = time
        continue

    if time - get_time >= c:
        candy_total += 1
        get_time = time
    else:
        continue

print(candy_total)
