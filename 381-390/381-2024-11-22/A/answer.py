N = int(input())
S = input()

if N % 2 == 0:
    print("No")
    exit()

half_minus = ((N+1)//2) -1
one = 0

for i in range(half_minus):
    if S[i] == "1":
        one += 1

if one != half_minus:
    print("No")
    exit()

half = (N + 1) // 2
if S[half-1] != "/":
    print("No")
    exit()

half_plus = (N+1)//2 + 1
two = 0

for i in range(half_minus):
    if S[half_plus-1+i] == "2":
        two += 1
if two != half_minus:
    print("No")
    exit()

print("Yes")