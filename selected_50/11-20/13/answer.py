n = int(input())
a_list = list(map(int, input().split()))
x = int(input())

a_sum = 0

for i in a_list:
    a_sum += i

a_list_least_number = x // a_sum

b_sum = a_sum * a_list_least_number
b_index = a_list_least_number * len(a_list)

for i in range(len(a_list)):
    b_sum += a_list[i]
    b_index += 1

    if b_sum > x:
        print(b_index)
        exit()



