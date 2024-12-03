N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(len(A)):
    if i+1 == len(A):
        break
    if A[i+1] > A[i]:
        A[i+1] = A[i]

A_val_idx = []
A_ext = []

for i in range(len(A)):
    if i == 0:
        A_val_idx.append([A[i], i])
        A_ext.append(A[i])
    else:
        if A[i-1] != A[i]:
            A_val_idx.append([A[i], i])
            A_ext.append(A[i])


def binary_search(numbers: list[int], value: int):
    left = 0
    right = len(numbers) - 1

    if value >= numbers[0]:
        return 0
    elif value < numbers[-1]:
        return -1

    while 1 < right - left:
        mid = (left+right)//2
        if value == numbers[mid]:
            return mid
        if numbers[mid] < value:
            right = mid
        else:
            left=mid

    return right

for i in range(len(B)):
    ans_idx = binary_search(A_ext, B[i])
    if ans_idx == -1:
        print(-1)
        continue
    
    ans = A_val_idx[ans_idx][1] +1
    print(ans)



#
# A_sorted = sorted(A_sorted, reverse=True, key=lambda x: x[0])

# A_sorted_one_gen = []

# for i in range(len(A_list)):
#     A_sorted_one_gen.append(A_sorted[i][0])

# while A_sorted_one_gen[0] > max(B_list):
#     A_sorted.remove(A_sorted[0][0])

# print(A_sorted)
# print(B_list)
# print("-----------------")    

# is_exit_no_eaten = True
# while is_exit_no_eaten:
#     if A_sorted[-1][0] < B_sorted[-1][0]:
#         B_sorted.remove(B_sorted[-1])
#     else:
#         is_exit = False

# A_sorted = []
# for i in range(len(A_list)):
#     A_sorted.append([A_list[i], i])

# B_sorted = []
# for i in range(len(B_list)):
#     B_sorted.append([B_list[i], i])

# A_sorted = sorted(A_sorted, reverse=True, key=lambda x: x[0])
# B_sorted = sorted(B_sorted, reverse=True, key=lambda x: x[0])

# is_exit = True
# while is_exit:
#     if A_sorted[0][0] > B_sorted[0][0]:
#         A_sorted.remove(A_sorted[0])
#     else:
#         is_exit = False

# for i in range(len(B_sorted)):
#     main_dish = B_sorted[i][0]
#     is_exit = True
#     eat_list = []
#     while is_exit:
#         if A_sorted[0][0] >= main_dish:
#             eat_list.append(A_sorted)
#         else:
#             eat_list = sorted(eat_list, key=lambda x: x[1])
            
        


# print(A_sorted)
# print(B_sorted)
# print("-----------------")  