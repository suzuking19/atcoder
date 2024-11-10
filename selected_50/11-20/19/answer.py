n, q = map(int, input().split())
a_list = list(map(int, input().split()))
a_list.sort()

for _ in range(q):
    x = int(input())
    left = 0
    right = len(a_list) - 1

    if x < a_list[left]:
        print(len(a_list))
        continue
    elif x > a_list[right]:
        print(0)
        continue

    while 1 < right - left:
        mid = (left + right) // 2

        if a_list[mid] < x:
            left = mid
        else:
            right = mid

    print(len(a_list)-right)