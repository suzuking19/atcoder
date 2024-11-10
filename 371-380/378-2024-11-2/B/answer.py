# N = int(input())

# garbages = []

# for _ in range(N):
#     q, r = map(int, input().split())
#     garbages.append([q, r])

# Q = int(input())

# questions = []

# for _ in range(Q):
#     t, d = map(int, input().split())
#     questions.append([t, d])


# for i in range(Q):
#     garbage_q = garbages[questions[i][0] - 1][0]
#     garbage_r = garbages[questions[i][0] - 1][1]
#     date = questions[i][1]

#     is_take = True

#     while is_take:
#         divide_date = date % garbage_q
#         if divide_date == garbage_r:
#             is_take = False
#             break
        
#         date += 1


#     print(date)

# TLEにならない回答
N = int(input())

q = [0] * N
r = [0] * N

for i in range(N):
    q[i], r[i] = map(int, input().split())

Q = int(input())
for _ in range(Q):
    t, d = map(int, input().split())

    # tをインデックスに対応させる
    t -= 1

    # b：商, c：あまり
    b, c = divmod(d, q[t])
    a = b if c <= r[t] else b + 1
    ans =a * q[t] + r[t]
    print(ans)
