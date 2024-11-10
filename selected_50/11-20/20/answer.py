n = int(input())
c_list = list(map(int, input().split()))

c_list.sort()

ans = 1

for i in range(n):

    if c_list[i] - i == 0:
        print(0)
        exit()

    ans *= c_list[i] - i
    ans %= 10**9+7

print(ans)
