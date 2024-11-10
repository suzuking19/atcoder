n = int(input())
a_list = list(map(int, input().split()))

total = 0

for i in a_list:
    if i >= 10:
        total += i -10

print(total)