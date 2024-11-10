n ,w = map(int, input().split())

cheese_list = []

for _ in range(n):
    a, b = map(int, input().split())
    cheese_list.append([a, b])

cheese_list.sort(reverse=True)

rest_cheese_grams = 0

for i in range(len(cheese_list)):
    rest_cheese_grams += cheese_list[i][1]

cheese_num = 0
total_delicious_grams = 0
total_delicious = 0

while total_delicious_grams < w and rest_cheese_grams > 0:
    total_delicious += cheese_list[cheese_num][0]
    cheese_list[cheese_num][1] -= 1
    total_delicious_grams += 1
    rest_cheese_grams -= 1

    if cheese_list[cheese_num][1] == 0:
        cheese_num += 1

print(total_delicious)

# 他の解答
N, W = map(int, input().split())

#チーズの情報
Cheese=[]

for i in range(N):
    A, B = map(int, input().split())
    Cheese.append([A,B])

Cheese.sor(reverse=True)

#答え
ans = 0

for i in range(N):
    Delicious = Cheese[i][0]
    Weight = Cheese[i][1]

    if Weight <= W:
        # 全部のせる
        ans += Delicious*Weight
        # のせられる残りの重さ
        W -= Weight
    else:
        # W[g]分のせる
        ans += Delicious*W
        # これ以上載せられないためforを抜ける
        break

print(ans)