from collections import defaultdict

n = int(input())
a_list = list(map(int, input().split()))

count = defaultdict(int)

for i in range(n):
    count[a_list[i]] +=1

all_pattern = n*(n-1)//2

for x in count.values():
    if x > 1:
        all_pattern -= x*(x-1)//2

print(all_pattern)






