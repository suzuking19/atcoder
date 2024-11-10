n = int(input())
s_list = list(map(int, input().split()))
t_list = list(map(int, input().split()))

# リストに初期値を持たせる
time = [10**15]*n

for i in range(n):
    if i == n-1:
        time[0] = min(t_list[0], time[i]+s_list[i])
        continue

    time[i+1] = min(t_list[i+1], time[i]+s_list[i])

for i in range(n):
    if i == n-1:
        time[0] = min(t_list[0], time[i]+s_list[i])
        continue

    time[i+1] = min(t_list[i+1], time[i]+s_list[i])

for i in range(n):
    print(time[i])