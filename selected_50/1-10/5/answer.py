s = input()

a = b = 0

for i in range(len(s)):
    if i == 0:
        a = int(s[i])
    elif i == 2:
        b = int(s[i])

print(a*b)

#　他の方法
s0=int(s[0])
s2=int(s[2])

print(s0*s2)