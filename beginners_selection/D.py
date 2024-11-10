# 用意する変数　２で割るカウント(count) 偶数カウント
# すべて偶数かを判定 
# 奇数が含まれる → print(count)を実行して処理を終了する
# すべて偶数 → 要素をすべて2で割る、偶数判定に戻る（再起関数）

def even_counter(len_list: int, int_list: list[int]) -> None:
    count_func = 0

    def _even_counter(len_list: int, int_list: list[int], count_func: int) -> None:
        count_even = 0
        for i in int_list:
            if i % 2 == 0:
                count_even += 1
            
        if count_even != len_list:
            print(count_func)
        
        elif count_even == len_list:
            count_func += 1

            for i in range(len(int_list)):
                int_list[i] = int_list[i] // 2

            _even_counter(len_list, int_list, count_func)
        
    _even_counter(len_list, int_list, count_func)


if __name__ == "__main__":
    N = int(input())
    int_list = list(map(int, input().split()))
    even_counter(N, int_list)
