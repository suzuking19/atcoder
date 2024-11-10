# 500円 100円 50円 それぞれを0から指定された枚数で全パターンで調べる
def coins(a: int, b:int, c:int, x:int) -> None:
    total_pattern = 0

    for i in range(0, a+1):
        for j in range(0, b+1):
            for k in range(0, c+1):
                if 500*i + 100*j + 50*k == x:
                    total_pattern += 1

    print(total_pattern)

if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    coins(A, B, C, X)
