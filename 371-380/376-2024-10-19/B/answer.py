# N, Q = map(int, input().split())

# total_move = 0

# L, R = 1, 2

# for i in range(Q):
#     H, T = map(str, input().split())
#     T = int(T)
#     move = 0
#     now = 0
#     goal = T

#     if H =="L":
#         now = L
#         while now != goal:
#             if now == N:
#                 now = 1
#             else: 
#                 now += 1
#             move += 1
#             if now == R:
#                 now = L
#                 move = 0
#                 break
        
#         while now != goal:
#             if now == 1:
#                 now = N
#             else:
#                 now -= 1
#             move += 1

#         total_move += move
#     else:
#         now = R
#         while now != goal:  
#             if now == N:
#                 now = 1
#             else: 
#                 now += 1
#             move += 1
#             if now == L:
#                 now = R
#                 move = 0
#                 break
        
#         while now != goal:
#             if now == 1:
#                 now = N
#             else:
#                 now -= 1
#             move += 1

#         total_move += move

# print(total_move)

def num_move(n, from_, to, ng):
    if from_ > to:
        from_, to = to, from_
    if from_ < ng < to:
        return n + from_ - to
    else:
        return to - from_
    

n, q = map(int, input().split())
l, r = 1, 2
total_move = 0

for i in range(q):
    h, t = map(str, input().split())
    t = int(t)

    if h == "L":
        total_move += num_move(n, l, t, r)
        l = t
    else:
        total_move += num_move(n, r, t, l)
        r = t

print(total_move)