s = input()
t = input()
n = min(len(s), len(t))
if s == t:
    print(0)
elif s[:n] == t[:n]:
    print(n+1)
else:
    for i in range(n):
        if s[i] != t[i]:
            print(i+1)
            break
