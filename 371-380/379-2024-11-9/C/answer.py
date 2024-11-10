N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

A_sum = sum(A)

if A_sum != N or X[0] != 1:
    print(-1)
    exit()

ans = 0

for i in range(len(X)):
    # 最後の要素
    if i == len(X) - 1:
        if X[i] == N:
            if A[i] == 1:
                break
            else:
                print(-1)
                exit()

        diff = N+1 - X[i]
        if A[i] == diff:
            if diff == 2:
                ans += 1
                break
            ans += diff * (diff + 1) // 2
            break
        else:
            print(-1)
            exit()
    # 最後以外の要素
    diff = X[i+1] - X[i]
    if A[i] == diff:
        if diff == 1:
            continue
        if diff == 2:
            ans += 1
            continue
        ans += diff * (diff + 1) // 2
    else:
        print(-1)
        exit()

print(ans)

# 4 -1 4 0 3
