# a, b, c = map(int, input().split())

# a_ex = pow(a, c)
# b_ex = pow(b, c)

# if a_ex > b_ex:
#     print(">")
# elif a_ex < b_ex:
#     print("<")
# else:
#     print("=")
# ↑これだとTLEになってしまうので違う処理を実装する

a, b, c = map(int, input().split())

if c % 2 != 0:
    if a >= 0:
        if b >= 0:
            if abs(a) > abs(b):print(">")
            if abs(a) == abs(b):print("=")
            if abs(a) < abs(b):print("<")
        elif b < 0:
            if abs(a) > abs(b):print(">")
            if abs(a) == abs(b):print(">")
            if abs(a) < abs(b):print(">")
    elif a < 0:
        if b >= 0:
            if abs(a) > abs(b):print("<")
            if abs(a) == abs(b):print("<")
            if abs(a) < abs(b):print("<")
        elif b < 0:
            if abs(a) > abs(b):print("<")
            if abs(a) == abs(b):print("=")
            if abs(a) < abs(b):print(">")
elif c % 2 == 0:
    if a >= 0:
        if b >= 0:
            if abs(a) > abs(b):print(">")
            if abs(a) == abs(b):print("=")
            if abs(a) < abs(b):print("<")
        elif b < 0:
            if abs(a) > abs(b):print(">")
            if abs(a) == abs(b):print("=")
            if abs(a) < abs(b):print("<")
    elif a < 0:
        if b >= 0:
            if abs(a) > abs(b):print(">")
            if abs(a) == abs(b):print("=")
            if abs(a) < abs(b):print("<")
        elif b < 0:
            if abs(a) > abs(b):print(">")
            if abs(a) == abs(b):print("=")
            if abs(a) < abs(b):print("<")
