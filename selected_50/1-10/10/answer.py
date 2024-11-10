# n = int(input())
# mountains_dict = {}

# for _ in range(n):
#     name, height = map(str, input().split())
#     height = int(height)
#     mountains_dict[name] = height

# max_value = max(mountains_dict.values())

# for i in mountains_dict:
#     if mountains_dict[i] == max_value:
#         break

# mountains_dict.pop(i)

# max_second_value = max(mountains_dict.values())

# for i in mountains_dict:
#     if mountains_dict[i] == max_second_value:
#         output = i

# print(output)

n = int(input())

mountains_list = []

for _ in range(n):
    s, t = map(str, input().split())
    t = int(t)
    # sortは各要素の最初の要素で比較されるので、heightを先にする
    mountains_list.append([t, s])

mountains_list.sort(reverse=True)
print(mountains_list[1][1])

