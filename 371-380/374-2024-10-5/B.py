# def equal_func(s: str, t: str) -> None:
#     if s == t:
#         print(0)

#     min_length = min(len(s), len(t))

#     for i in range(min_length):
#         if s[i] != t[i]:
#             print(i+1)
#             return

#     if len(s) > len(t):
#         print(len(t)+1)
#         return
#     elif len(s) < len(t):
#         print(len(s)+1)
#         return 



# S = str(input())
# T = str(input())
# equal_func(S, T)

import math

n = int(input())

total = 0

pre_x = pre_y = 0

for i in range(n):
    x, y = map(int, input().split())

    total += math.sqrt(((x-pre_x)**2) + ((y-pre_y)**2))

    pre_x, pre_y = x, y

    if i == n-1:
        total += math.sqrt((x**2) + (y**2))

print(total)