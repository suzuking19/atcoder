# リストから最大値を取得する
# リスト内に最大値と同じ値があれば削除する

def rice_cake_counter(rice_cake_list: list[int]) -> int:
    count = 0
    while len(rice_cake_list) > 0:
        largest_rice_cake = max(rice_cake_list)
        count += 1
        rice_cake_list = [x for x in rice_cake_list if x != largest_rice_cake]

    return count

if __name__ == "__main__":
    N = int(input())
    rice_cake_list = []
    for i in range(N):
        rice_cake = int(input())
        rice_cake_list.append(rice_cake)
    print(rice_cake_counter(rice_cake_list))
