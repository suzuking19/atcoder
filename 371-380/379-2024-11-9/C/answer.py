# N, M = map(int, input().split())
# X = list(map(int, input().split()))
# A = list(map(int, input().split()))

# A_sum = sum(A)

# if A_sum != N or X[0] != 1:
#     print(-1)
#     exit()

# ans = 0

# for i in range(len(X)):
#     # 最後の要素
#     if i == len(X) - 1:
#         if X[i] == N:
#             if A[i] == 1:
#                 break
#             else:
#                 print(-1)
#                 exit()

#         diff = N+1 - X[i]
#         if A[i] == diff:
#             if diff == 2:
#                 ans += 1
#                 break
#             ans += diff * (diff + 1) // 2
#             break
#         else:
#             print(-1)
#             exit()
#     # 最後以外の要素
#     diff = X[i+1] - X[i]
#     if A[i] == diff:
#         if diff == 1:
#             continue
#         if diff == 2:
#             ans += 1
#             continue
#         ans += diff * (diff + 1) // 2
#     else:
#         print(-1)
#         exit()

# print(ans)

# 4 -1 4 0 3
N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

# 石の合計がN個かを判定
if sum(A) != N:
    print(-1)
    exit()

# 辞書に石の数を登録
stone_num_dict = {}
for i in range(len(X)):
    stone_num_dict[X[i]] = A[i]

ans = 0

# Xを昇順にソート
X.sort()


for i in range(len(X)):
    # 石の数
    stone_num = stone_num_dict[X[i]]

    # 最後のXの場合
    if i == len(X) -1:
        # 最後尾との差
        diff = N+1 - X[i]
        
        # Xが最後尾だった場合
        if diff == 1:
            # 石の数が適切かを判定 
            if stone_num == 1:
                break
            else:
                print(-1)
                exit()
        
        # 必要な石の数ぴったりだった場合
        if stone_num == diff:
            ans += (diff-1)*diff//2
            break
        else:
            print(-1)
            exit()

    
    diff = X[i+1] - X[i]
    if stone_num >= diff:
        ans += (diff-1)*diff//2 + (stone_num - diff) * diff
        stone_num_dict[X[i+1]] += stone_num - diff
    else:
        print(-1)
        exit()

print(ans)