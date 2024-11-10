n = input()

ans = 0

# 2^nパターンを検証
for bitnum in range(1<<len(n)):

    A = []
    B = []

    # 右シフト算で各数字が0か1か判定する
    for shift in range(len(n)):

        # 0ならば
        if bitnum >> shift & 1 == 0:
            A.append(n[shift])
        
        # 1ならば
        else:
            B.append(n[shift])

    # A,Bどちらかが空なら
    if A==[] or B==[]:
        continue

    # A,Bどちらも降順にソートして文字列に変換すれば積が最大値になる
    A.sort(reverse=True)
    B.sort(reverse=True)

    A_join = "".join(A)
    B_join = "".join(B)

    ans = max(ans, int(A_join)*int(B_join))

print(ans)
