# 商が0になるまで10で割り続けて、桁の和を求める関数を作成
def some_sums(N: int, A: int, B: int) -> None:
    total = 0
    for i in range(1, N+1):
        number = i
        rem = 0
        digit_total = 0
        while number > 0:
            rem = number % 10
            digit_total += rem
            number = number // 10
        
        if A <= digit_total <= B:
            total += i

    print(total)
            

if __name__ == "__main__":
    N, A, B = map(int, input().split())
    some_sums(N, A, B)