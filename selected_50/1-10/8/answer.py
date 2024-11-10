n = int(input())
a_list = list(map(int, input().split()))
# numbers = []
# total = 0

# for a in a_list:
#     if a not in numbers:
#         total += 1
#         numbers.append(a)
#     else:
#         continue

# print(total)

# setを使用する場合
# setの作成
# setX = set()

# セットへの要素の追加
# リストをセットにするには変数名=set(リスト)とすればよい

aSet = set(a_list)
print(len(aSet))