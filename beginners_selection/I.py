# それぞれのお札を通りの時で想定する for文を三重にする
def money_counter(number: int, amount: int) -> list[int]:
    for i in range(0, number+1):
        for j in range(0, number+1-i):  
            for k in range(0, number+1-i-j):
                if 10000*i + 5000*j + 1000*k == amount:
                    if i + j + k == number:
                        return [i, j, k]
                
    return [-1, -1, -1]


if __name__ == "__main__":
    N, Y = map(int, input().split())
    result = money_counter(N, Y)
    ten_thousand, five_thousand, thousand = result[0], result[1], result[2]
    print(ten_thousand, five_thousand, thousand)
