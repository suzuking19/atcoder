# s_list = list(map(str, input().split()))


# # < < <
# if s_list == ["<", "<", "<"]:
#     print("B")
# # > < <
# elif s_list == [">", "<", "<"]:
#     print("A")
# # < > < → 矛盾パターン
# elif s_list == ["<", ">", "<"]:
#     print("")
# # < < > 
# elif s_list == ["<", "<", ">"]:
#     print("C")
# # > > <
# elif s_list == [">", ">", "<"]:
#     print("C")
# # < > >
# elif s_list == ["<", ">", ">"]:
#     print("A")
# # > < > → 矛盾パターン
# elif s_list == [">", "<", ">"]:
#     print("")
# # > > >
# elif s_list == [">", ">", ">"]:
#     print("B")

"""
・S(AB) == S(AC) が成り立つ
    ・S(BC)の結果によって次男を判定
・S(AB) != S(AC)が成り立つ
    ・次男はAである
"""

s_list = list(map(str, input().split()))

if s_list[0] == s_list[1]:
    if s_list[0] == "<":
        if s_list[2] == "<":
            print("B")
        else:
            print("C")
    else:
        if s_list[2] == ">":
            print("B")
        else:
            print("C")
else:
    print("A")